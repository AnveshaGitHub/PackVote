import json
import os
from datetime import datetime

EXPENSES_FILE = os.path.join(os.path.dirname(__file__), 'data', 'expenses.json')

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return {'groups': {}}

def save_expenses(data):
    os.makedirs(os.path.dirname(EXPENSES_FILE), exist_ok=True)
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_expense(group_id, paid_by, amount, description, category, split_among, split_type='equal'):
    data = load_expenses()
    if group_id not in data['groups']:
        data['groups'][group_id] = {'expenses': [], 'members': split_among}

    amount = float(amount)

    # Calculate splits
    splits = {}
    if split_type == 'equal':
        per_person = round(amount / len(split_among), 2)
        for member in split_among:
            splits[member] = per_person
    else:
        # Custom split passed directly
        splits = split_among

    expense = {
        'id':          f"exp_{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        'paid_by':     paid_by,
        'amount':      amount,
        'description': description,
        'category':    category,
        'split_among': split_among if isinstance(split_among, list) else list(split_among.keys()),
        'splits':      splits,
        'split_type':  split_type,
        'date':        datetime.now().strftime('%Y-%m-%d'),
        'created_at':  datetime.now().isoformat()
    }

    data['groups'][group_id]['expenses'].append(expense)
    save_expenses(data)
    return {'success': True, 'expense': expense}

def get_expenses(group_id):
    data = load_expenses()
    if group_id not in data['groups']:
        return {'expenses': [], 'summary': {}, 'settlements': []}

    expenses = data['groups'][group_id]['expenses']
    summary  = calculate_summary(expenses)
    settlements = calculate_settlements(summary['balances'])

    return {
        'expenses':    expenses,
        'summary':     summary,
        'settlements': settlements
    }

def calculate_summary(expenses):
    total_spent    = 0
    by_category    = {}
    by_person_paid = {}
    by_person_owed = {}
    balances       = {}

    for exp in expenses:
        amount  = exp['amount']
        paid_by = exp['paid_by']
        splits  = exp['splits']

        total_spent += amount

        # Category breakdown
        cat = exp.get('category', 'other')
        by_category[cat] = by_category.get(cat, 0) + amount

        # Who paid
        by_person_paid[paid_by] = by_person_paid.get(paid_by, 0) + amount

        # Balances — payer gets credited, others get debited
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
    """
    Minimum transactions algorithm.
    Figures out the simplest way for everyone to settle up.
    """
    creditors = []  # people who are owed money
    debtors   = []  # people who owe money

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
    data = load_expenses()
    if group_id not in data['groups']:
        return {'success': False, 'error': 'Group not found'}

    expenses = data['groups'][group_id]['expenses']
    data['groups'][group_id]['expenses'] = [
        e for e in expenses if e['id'] != expense_id
    ]
    save_expenses(data)
    return {'success': True}

def get_expense_stats(group_id):
    data     = load_expenses()
    if group_id not in data['groups']:
        return {}
    expenses = data['groups'][group_id]['expenses']
    if not expenses:
        return {}
    summary  = calculate_summary(expenses)
    biggest  = max(expenses, key=lambda x: x['amount'])
    return {
        'total_spent':    summary['total_spent'],
        'total_expenses': len(expenses),
        'biggest_expense': {
            'description': biggest['description'],
            'amount':      biggest['amount'],
            'paid_by':     biggest['paid_by']
        },
        'most_spent_category': max(summary['by_category'], key=summary['by_category'].get) if summary['by_category'] else '—',
        'biggest_spender':     max(summary['by_person_paid'], key=summary['by_person_paid'].get) if summary['by_person_paid'] else '—',
    }