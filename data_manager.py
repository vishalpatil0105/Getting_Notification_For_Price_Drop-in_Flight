# This Class is used for getting data from our google sheet in which we entered
# our destination and their low price

# module
import requests

# API END POINT
SHETTY_ENDPOINT = "https://api.sheety.co/6c47ce8ae18b53664d39007a9924b720/copyOfFlightDeals/prices"


class DataManager:
    def __init__(self):
        self.data = {}

    # Getting data from our google sheet via SHEETY API
    def get_data_from_sheet(self):
        sheet_data = requests.get(url=SHETTY_ENDPOINT)
        data = sheet_data.json()
        self.data = data["prices"]
        return self.data

    # PUTTING IATA CODE FOR EACH CITY IN SHEET
    def put_data(self):
        for city in self.data:
            new_data = {
                "price":
                {
                "iataCode": city["iataCode"]
                }
            }
            put_data_sheet = requests.put(url=f"{SHETTY_ENDPOINT}/{city['id']}", json=new_data)




