# THIS CLASS IS FOR CREATING USER

# Module
import requests

# SHEETY API
SHEET_API = "https://api.sheety.co/6c47ce8ae18b53664d39007a9924b720/copyOfFlightDeals/userData"


class PutUserData:
    # THIS PARAMETERS WILL GET PASS VAIA MAIN FILE
    def __init__(self, first_name, last_name, email):
        self.user_name = first_name
        self.last_name = last_name
        self.email = email

    # THIS FUNCTION IS FOR PASSING PARAMETERS TO USERDATA google sheet
    def put_data(self):
        param = {
            "userDatum": {
                "firsatName": self.user_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        # PASSING DATA TO google sheet via requests
        response_from_sheety = requests.post(url=SHEET_API, json=param)

