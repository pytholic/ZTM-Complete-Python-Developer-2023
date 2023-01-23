"""
Python script to send email.

Recently in google, we need to create 'App Passwords' now for third party apps
    - Go to gmail → account → security → App Passwords
    - Also need 'Two Factor Authentication' activated for that
"""

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Haseeb Raja"
email["to"] = "rajahaseeb147147@gmail.com"
email["Subject"] = "Testing"

email.set_content(html.substitute(name="TinTin"), "html")  # can add multiple arguments

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # for secure connection
    smtp.login("rajahaseeb147147@gmail.com", "iwsovpbxedxeprjn")
    smtp.send_message(email)
    print("Email sent!")
