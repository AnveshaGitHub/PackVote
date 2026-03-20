# email_service.py — place in backend/ folder
# Uses Gmail SMTP — completely free, no API key needed
# Setup: enable "App Password" in your Gmail account (2FA required)
# Go to: Google Account → Security → App Passwords → create one for "Mail"

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText


GMAIL_USER     = os.environ.get('GMAIL_USER',     'projectcheck1213@gmail.com')   # your@gmail.com
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', 'wopu wyka rztq hfvc')   # 16-char app password


def _send(to_email: str, subject: str, html_body: str) -> bool:
    """Core send function. Returns True on success."""
    if not GMAIL_USER or not GMAIL_PASSWORD:
        print("⚠️  Email not configured — skipping email send")
        return False
    if not to_email or '@' not in to_email:
        return False
    try:
        msg                    = MIMEMultipart('alternative')
        msg['Subject']         = subject
        msg['From']            = f"PackVote ✈ <{GMAIL_USER}>"
        msg['To']              = to_email
        msg.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, to_email, msg.as_string())

        print(f"✅ Email sent to {to_email}: {subject}")
        return True
    except Exception as e:
        print(f"❌ Email error: {e}")
        return False


# ── Email templates ───────────────────────────────────────────────────────

def send_join_confirmation(to_email: str, member_name: str,
                           group_name: str, group_id: str) -> bool:
    """Sent when a member joins a group."""
    subject = f"You joined '{group_name}' on PackVote ✈"
    html    = f"""
    <div style="font-family:Arial,sans-serif;max-width:560px;margin:0 auto;background:#0a0a0f;color:#ffffff;border-radius:12px;overflow:hidden;">
      <div style="background:linear-gradient(135deg,#6c63ff,#ff6584);padding:32px;text-align:center;">
        <h1 style="margin:0;font-size:2rem;">PackVote ✈</h1>
        <p style="margin:8px 0 0;opacity:0.9;">Vote. Plan. Travel.</p>
      </div>
      <div style="padding:32px;">
        <h2 style="color:#ffffff;margin-top:0;">Hey {member_name}! 👋</h2>
        <p style="color:#aaa;line-height:1.7;">
          You've successfully joined the travel group <strong style="color:#6c63ff;">"{group_name}"</strong>.
          The group creator is adding destinations for you to vote on.
        </p>
        <div style="background:#1a1a2e;border:1px solid #333;border-radius:10px;padding:20px;margin:24px 0;">
          <div style="font-size:0.85rem;color:#888;margin-bottom:4px;">Your Group ID</div>
          <div style="font-size:1.3rem;font-weight:700;color:#6c63ff;letter-spacing:2px;">{group_id}</div>
          <div style="font-size:0.8rem;color:#888;margin-top:8px;">Share this ID with other members so they can join too</div>
        </div>
        <p style="color:#aaa;line-height:1.7;">
          You'll receive another email when voting opens. Keep an eye on your inbox!
        </p>
        <div style="text-align:center;margin-top:24px;">
          <a href="http://127.0.0.1:5500/frontend/vote.html"
             style="background:linear-gradient(135deg,#6c63ff,#ff6584);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:700;display:inline-block;">
            Go to Vote Page ✈
          </a>
        </div>
      </div>
      <div style="padding:20px;text-align:center;color:#555;font-size:0.8rem;border-top:1px solid #222;">
        PackVote — Built with ❤️ for group travellers
      </div>
    </div>
    """
    return _send(to_email, subject, html)


def send_voting_open(to_email: str, member_name: str,
                     group_name: str, destinations: list) -> bool:
    """Sent to all members when creator opens voting."""
    dest_list = ''.join([
        f'<li style="padding:6px 0;color:#ccc;border-bottom:1px solid #333;">'
        f'<span style="color:#6c63ff;">✈</span> {d}</li>'
        for d in destinations
    ])
    subject = f"🗳️ Voting is open in '{group_name}'!"
    html    = f"""
    <div style="font-family:Arial,sans-serif;max-width:560px;margin:0 auto;background:#0a0a0f;color:#ffffff;border-radius:12px;overflow:hidden;">
      <div style="background:linear-gradient(135deg,#6c63ff,#ff6584);padding:32px;text-align:center;">
        <h1 style="margin:0;font-size:2rem;">PackVote ✈</h1>
        <p style="margin:8px 0 0;opacity:0.9;">Voting is now open!</p>
      </div>
      <div style="padding:32px;">
        <h2 style="color:#ffffff;margin-top:0;">Hey {member_name}! 🗳️</h2>
        <p style="color:#aaa;line-height:1.7;">
          The group <strong style="color:#6c63ff;">"{group_name}"</strong> is ready to vote!
          Here are the destinations your group is considering:
        </p>
        <ul style="list-style:none;padding:0;background:#1a1a2e;border-radius:10px;padding:16px 20px;margin:20px 0;">
          {dest_list}
        </ul>
        <p style="color:#aaa;">Vote now and help your group decide where to go!</p>
        <div style="text-align:center;margin-top:24px;">
          <a href="http://127.0.0.1:5500/frontend/vote.html"
             style="background:linear-gradient(135deg,#43e97b,#38f9d7);color:#0a0a0f;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:700;display:inline-block;">
            Cast My Vote Now 🗳️
          </a>
        </div>
      </div>
      <div style="padding:20px;text-align:center;color:#555;font-size:0.8rem;border-top:1px solid #222;">
        PackVote — Built with ❤️ for group travellers
      </div>
    </div>
    """
    return _send(to_email, subject, html)


def send_results_ready(to_email: str, member_name: str,
                       group_name: str, winner: str,
                       total_votes: int) -> bool:
    """Sent to all members when all votes are in."""
    subject = f"🏆 Results are in for '{group_name}'!"
    html    = f"""
    <div style="font-family:Arial,sans-serif;max-width:560px;margin:0 auto;background:#0a0a0f;color:#ffffff;border-radius:12px;overflow:hidden;">
      <div style="background:linear-gradient(135deg,#f7971e,#ffd200);padding:32px;text-align:center;">
        <h1 style="margin:0;font-size:2rem;color:#0a0a0f;">PackVote ✈</h1>
        <p style="margin:8px 0 0;color:#333;">The results are in!</p>
      </div>
      <div style="padding:32px;">
        <h2 style="color:#ffffff;margin-top:0;">Hey {member_name}! 🎉</h2>
        <p style="color:#aaa;line-height:1.7;">
          All {total_votes} members of <strong style="color:#ffd200;">"{group_name}"</strong> have voted.
          Your group is going to...
        </p>
        <div style="background:linear-gradient(135deg,rgba(108,99,255,0.2),rgba(255,101,132,0.15));
                    border:1px solid rgba(108,99,255,0.4);border-radius:12px;
                    padding:28px;text-align:center;margin:24px 0;">
          <div style="font-size:0.85rem;color:#aaa;margin-bottom:8px;">Your destination is</div>
          <div style="font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,#6c63ff,#ff6584);
                      -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            {winner}
          </div>
          <div style="font-size:0.85rem;color:#888;margin-top:8px;">
            Chosen by {total_votes} travellers
          </div>
        </div>
        <div style="text-align:center;margin-top:24px;">
          <a href="http://127.0.0.1:5500/frontend/results.html"
             style="background:linear-gradient(135deg,#6c63ff,#ff6584);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:700;display:inline-block;">
            View Full Itinerary 🗺️
          </a>
        </div>
      </div>
      <div style="padding:20px;text-align:center;color:#555;font-size:0.8rem;border-top:1px solid #222;">
        PackVote — Built with ❤️ for group travellers
      </div>
    </div>
    """
    return _send(to_email, subject, html)