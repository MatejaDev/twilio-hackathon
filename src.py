from twilio.rest import Client
import time
sms = True #set to False if you would like to recieve a phone call
phoneNumber = "" #set your phone number with a country code
fromPhoneNumber = "" #set from phone number with a country code

client = Client("account_sid", "auth_token")

while True:
    if sms:
        message = client.messages \
            .create(
                 body='Please wash your hands. ',
                from_=fromPhoneNumber,
                 to=phoneNumber
            )
    else:
        call = client.calls.create(
                        twiml='<Response><Say>Please wash your hands, thank you!</Say></Response>',
                        to=phoneNumber,
                        from_=fromPhoneNumber
                    )
    print("Successfully sent!")
    time.sleep(30*60)
