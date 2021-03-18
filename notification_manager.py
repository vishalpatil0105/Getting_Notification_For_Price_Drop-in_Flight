# THIS CLASS IS ALL ABOUT SENDING AN EMAIL WHENEVER PRICE DROP

# Module
import smtplib
import requests

# SHEET API
SHEET_API = "https://api.sheety.co/6c47ce8ae18b53664d39007a9924b720/copyOfFlightDeals/userData"

# PASS FOR GOOGLE ACC FROM {IT's KIND OF  your email from which you can send email to all client to inform price has
# been dropped
# {THERE ARE MULTIPLE SETTINGS WHICH WE HAVE TO DO BEFORE SENDING AN EMAIL VIA SMTP PLEASE DO STACKOVERFLOW SEARCH FOR
# MORE}
MY_PASS = "vishal@1998" # ENTER YOUR PASS
MY_EMAIL = "brocumon6969@gmail.com" # ENTER YOUR EMAIL
MESSGAE = "Price Has been dropped for flight"


class NotificationManager:

    # THIS FUNCTION WILL SEND AN EMAIL WHENEVER PRICE DROP
        def send_email(self, city):
            # GETTING DATA FROM SHEET
            response_from_sheet = requests.get(url=SHEET_API)
            data = response_from_sheet.json()["userData"]
            for user_data in data:
                name = user_data["firsatName"]
                last_name = user_data["lastName"]
                email = user_data["email"]

                # SENDING EMAIL TO EACH EMAIL IN OUR SHEET WITH THEIR NAME AND MESSAGE
                # {read smtplib module to understand this if you are unfamiliar with smtplib}
                with smtplib.SMTP("gmail.com") as connection:
                    connection.starttls()
                    connection.login(MY_EMAIL, MY_PASS)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:FLIGHT PRICE DROPPED!\n\nDear{name} {last_name}\n{MESSGAE} for {city} city\n".encode('utf-8')
                        )

