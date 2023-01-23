"""
Python script to send email.

Recently in google, we need to create 'App Passwords' now for third party apps
    - Go to gmail → account → security → App Passwords
    - Also need 'Two Factor Authentication' activated for that
"""

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Haseeb Raja"
email["to"] = "******"
email["Subject"] = "Testing"

email.set_content("Sending email using Python.")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # for secure connection
    smtp.login("rajahaseeb147147@gmail.com", "******")
    smtp.send_message(email)
    print("Email sent!")
