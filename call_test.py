# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from os import environ


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = environ['ACCT_KEY']
auth_token = environ['AUTH_KEY']
client = Client(account_sid, auth_token)

message = client.calls.create(
                     url = "http://demo.twilio.com/docs/voice.xml",
                     from_= environ['TWILLIO_NUMBER'],
                     to= environ['MY_NUMBER']
                     )
