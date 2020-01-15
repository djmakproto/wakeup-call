# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from os import environ
import time


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = environ['ACCT_KEY']
auth_token = environ['AUTH_KEY']
client = Client(account_sid, auth_token)

while True:
  tm = time.gmtime()
  hr = tm.tm_hour-5
  day = tm.tm_wday
  print("hr: " + str(hr))
  print("day: " + str(day))
  if(hr == 7 and day < 5):
    print("calling...")
    message = client.calls.create(
      twiml = "<Response><Say voice=\"alice\">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</Say></Response>",
      from_= envrion['TWILLIO_NUMBER'],
      to= environ['MY_NUMBER'])
  time.sleep(60*15)
