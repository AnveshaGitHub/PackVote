import json
from datetime import datetime
from database import execute_query, execute_one

def add_expense(group_id, paid_by, amount, description, category, split_among, split_type='equal'):
    amount = float(amount)

    # Calculate splits
    splits = {}
    if split_type == 'equal':
        members    = split_among if isinstance(split_among, list) else list(split_among.keys())
        per_person = round(amount / len(members), 2)
        for member in members:
            splits[member] = per_person
    else:
        splits  = split_among
        members = list(split_among.keys())

    expense_id = f"exp_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

    execute_query("""
        INSERT INTO expenses
            (expense_id, group_id, paid_by, amount, description,
             category, split_among, splits, split_type, expense_date, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        expense_id, group_id, paid_by, amount, description,
        category,
        json.dumps(members),
        json.dumps(splits),
        split_type,
        datetime.now().date(),
        datetime.now()
    ))

    return {
        'success': True,
        'expense': {
            'id':          expense_id,
            'paid_by':     paid_by,
            'amount':      amount,
            'description': description,
            'category':    category,
            'split_among': members,
            'splits':      splits,
            'split_type':  split_type,
            'date':        str(datetime.now().date())
        }
    }


def get_expenses(group_id):
    rows = execute_query(
        "SELECT * FROM expenses WHERE group_id = %s ORDER BY created_at DESC",
        (group_id,), fetch=True
    ) or []

    expenses = []
    for row in rows:
        try:
            split_among = json.loads(row['split_among'] or '[]')
            splits      = json.loads(row['splits']      or '{}')
        except:
            split_among = []
            splits      = {}

        expenses.append({
            'id':          row['expense_id'],
            'paid_by':     row['paid_by'],
            'amount':      float(row['amount']),
            'description': row['description'],
            'category':    row['category'],
            'split_among': split_among,
            'splits':      splits,
            'split_type':  row['split_type'],
            'date':        str(row['expense_date'])
        })

    summary     = calculate_summary(expenses)
    settlements = calculate_settlements(summary['balances'])

    return {
        'expenses':    expenses,
        'summary':     summary,
        'settlements': settlements
    }


def calculate_summary(expenses):
    if not expenses:
        return get_empty_summary()

    total_spent    = 0
    by_category    = {}
    by_person_paid = {}
    balances       = {}

    for exp in expenses:
        amount  = exp['amount']
        paid_by = exp['paid_by']
        splits  = exp['splits']

        total_spent += amount

        by_category[exp['category']] = by_category.get(exp['category'], 0) + amount
        by_person_paid[paid_by]      = by_person_paid.get(paid_by, 0) + amount

        if paid_by not in balances:
            balances[paid_by] = 0
        balances[paid_by] += amount

        for member, share in splits.items():
            if member not in balances:
                balances[member] = 0
            balances[member] -= share

    return {
        'total_spent':    round(total_spent, 2),
        'per_person_avg': round(total_spent / max(len(balances), 1), 2),
        'by_category':    {k: round(v, 2) for k, v in by_category.items()},
        'by_person_paid': {k: round(v, 2) for k, v in by_person_paid.items()},
        'balances':       {k: round(v, 2) for k, v in balances.items()},
        'total_expenses': len(expenses)
    }


def calculate_settlements(balances):
    creditors = []
    debtors   = []

    for person, balance in balances.items():
        if balance > 0.01:
            creditors.append([person, balance])
        elif balance < -0.01:
            debtors.append([person, -balance])

    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1],   reverse=True)

    settlements = []
    i, j = 0, 0

    while i < len(creditors) and j < len(debtors):
        creditor = creditors[i]
        debtor   = debtors[j]
        amount   = min(creditor[1], debtor[1])

        settlements.append({
            'from':   debtor[0],
            'to':     creditor[0],
            'amount': round(amount, 2)
        })

        creditor[1] -= amount
        debtor[1]   -= amount

        if creditor[1] < 0.01: i += 1
        if debtor[1]   < 0.01: j += 1

    return settlements


def delete_expense(group_id, expense_id):
    existing = execute_one(
        "SELECT expense_id FROM expenses WHERE expense_id = %s AND group_id = %s",
        (expense_id, group_id)
    )
    if not existing:
        return {'success': False, 'error': 'Expense not found'}

    execute_query(
        "DELETE FROM expenses WHERE expense_id = %s AND group_id = %s",
        (expense_id, group_id)
    )
    return {'success': True}


def get_expense_stats(group_id):
    data = get_expenses(group_id)
    expenses = data['expenses']
    if not expenses:
        return {}

    summary = data['summary']
    biggest = max(expenses, key=lambda x: x['amount'])

    return {
        'total_spent':         summary['total_spent'],
        'total_expenses':      len(expenses),
        'biggest_expense': {
            'description': biggest['description'],
            'amount':      biggest['amount'],
            'paid_by':     biggest['paid_by']
        },
        'most_spent_category': max(summary['by_category'], key=summary['by_category'].get) if summary['by_category'] else '—',
        'biggest_spender':     max(summary['by_person_paid'], key=summary['by_person_paid'].get) if summary['by_person_paid'] else '—',
    }


def get_empty_summary():
    return {
        'total_spent':    0,
        'per_person_avg': 0,
        'by_category':    {},
        'by_person_paid': {},
        'balances':       {},
        'total_expenses': 0
    }