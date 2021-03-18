# THIS IS A MAIN FILE FROM WHERE WE ARE HANDLING ALL OUR CODE

# importing all our modules

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from Put_user_data import PutUserData

# FROM DATA MANAGER CLASS WE ARE GETTING NEW DATA {REFER DATA_MANAGER CLASS}
data_manager = DataManager()

# THIS WILL RETURN NEW DATA WITH IATA CODE
return_data = data_manager.get_data_from_sheet()

# CREATING OBJECTS OF FLIGHT_SEARCH AND Notification_manager class
flight_search = FlightSearch()
send_notification = NotificationManager()

# GETTING input from user and this information will get stored in google sheet
USERNAME = input("Enter your First name: ")
LAST_NAME = input("Enter Your Last_name: ")
EMAIL = input("Enter Your last_name: ")

# Storing data into google sheet
put_user_data = PutUserData(first_name=USERNAME, last_name=LAST_NAME, email=EMAIL)
put_user_data.put_data()

# THIS VARIABLE CONTAIN IATA CODE OF OUR CURRENT CITY FROM WHERE WE WANT TO TRAVEL ITS BOM NOW for MUMBAI
ORIGIN_CITY_IATA = "BOM"

# WHEN WE 1st crate sheet there will be no iata code for cities so if its not their then this block will execute
if return_data[0]["iataCode"] == "":

    # WE WILL FEATCH get_flight_data function form flightsearch class to get iata code for each city
    from_flight_search = FlightSearch()
    for data in return_data:
        data["iataCode"] = from_flight_search.get_flight_data(data["city"])

    # after execution of this we are replacing our data_manager.data variable with return data from above function
    # with iata code for each country
    data_manager.data = return_data

    # AFTER THAT CALLING put_data function from data_manager for storing data into sheet
    data_manager.put_data()

# Getting todays date and price for next 6 month using timedelta function
tomorrow = datetime.now() + timedelta(days=1)
next_6_month = datetime.now() + timedelta(days=(6 * 30))

# This will pass each city iata and time to search flight_fuction
for city in return_data:
    flight = flight_search.search_flight(
        ORIGIN_CITY_IATA,
        city["iataCode"],
        from_time=tomorrow,
        to_time=next_6_month
    )
    # if flight_search return none then this will just pass
    if flight is None:
        pass

    # else this will go ahead and compare current price of ticket and all time low price which
    # we stored in google sheet
    else:

        # its matches then it will send an email to all the emails in our user_data google sheet
        if flight.price < city["lowestPrice"]:
            send_notification.send_email(city["city"])





