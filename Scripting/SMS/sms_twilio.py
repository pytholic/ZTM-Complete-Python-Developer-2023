# Download the helper library from https://www.twilio.com/docs/python/install
import os
import yaml
from twilio.rest import Client

with open("config.yaml") as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(e)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config["TWILIO_ACCOUNT_SID"]
auth_token = config["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hi there", from_="+17432553097", to="+821097727005"
)

print(message.sid)
