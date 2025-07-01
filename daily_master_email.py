import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# CONFIG
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

# Load today's index
DAY_INDEX = (datetime.utcnow().date() - datetime(2025, 7, 1).date()).days

# Load content from JSON
base_path = "data"

def load_json(filename):
    with open(os.path.join(base_path, filename), 'r') as f:
        return json.load(f)

billionaire = load_json("billionaires.json")[DAY_INDEX]
french = load_json("daily_french.json")[DAY_INDEX]
opps = load_json("daily_opportunities.json")[DAY_INDEX]
gmat = load_json("daily_gmat_logic_mechanical.json")[DAY_INDEX]
technical = load_json("daily_technical_insights.json")[DAY_INDEX]
health = load_json("daily_health_and_lifehacks.json")[DAY_INDEX]

# Create email content
html = f"""
<h2>✨ Day {DAY_INDEX+1} Mastery Email</h2>

<h3>📈 Billionaire Inspiration</h3>
<b>{billionaire['name']}</b><br>
<blockquote>{billionaire['quote']}</blockquote>
<a href="{billionaire['video_link']}">Watch Video</a> | <a href="{billionaire['article_link']}">Read Article</a><br>
<small>{billionaire['tip']}</small>

<h3>🌐 French B2 Practice ({french['level']})</h3>
<ul>
<li><b>Reading:</b> {french['reading']}</li>
<li><b>Writing:</b> {french['writing']}</li>
<li><b>Listening:</b> <a href="{french['listening']}">Audio</a></li>
<li><b>Speaking:</b> {french['speaking']}</li>
</ul>

<h3>📅 Scholarships/Conferences</h3>
<ul>
{''.join([f'<li><b>{op["title"]}</b> - Deadline: {op["deadline"]}<br><a href="{op["link"]}">Apply</a></li>' for op in opps])}
</ul>

<h3>🧠 Engineering Case Study</h3>
<b>{technical['topic']}</b><br>
<i>{technical['scenario']}</i><br>
<p>{technical['insight']}</p>
<b>Quiz:</b> {technical['quiz']['question']}<br>
<i>Answer:</i> {technical['quiz']['answer']}

<h3>🎯 GMAT + Logic + Mechanical</h3>
<ul>
<li><b>GMAT:</b> {gmat['gmat']['question']}<br><i>{gmat['gmat']['solution']}</i></li>
<li><b>Logic:</b> {gmat['logic']['puzzle']}<br><i>{gmat['logic']['solution']}</i></li>
<li><b>Mechanical:</b> {gmat['mechanical']['question']}<br><i>{gmat['mechanical']['solution']}</i></li>
</ul>

<h3>💪 Health + Life Tip</h3>
<b>Health:</b> {health['health_tip']}<br>
<b>Life Hack:</b> {health['life_hack']}

<p><i>Keep pushing. You’re {DAY_INDEX+1}% through your 100-day mastery journey.</i></p>
"""

# Send the email
def send_email():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Day {DAY_INDEX+1} - Your AutoBillionaire Growth Toolkit"
    msg['From'] = GMAIL_USER
    msg['To'] = TO_EMAIL
    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_USER, GMAIL_PASS)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    send_email()
