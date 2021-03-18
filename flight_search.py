# IN THIS CLASS WE ARE SEARCHING FLIGHT AND GETTING IATA CODE FOR EACH CITY IN OUR SHEET

# Modules
import requests
from flight_data import FlightData

# THIS APIKEY YOU WILL GET AFTER LOGIN INTO TAQUILA API SITE
# THIS IS USED TO GET IATA CODE FOR EACH COUNTRY/CITY
FLIGHT_SEARCH_API = {"apikey": "BoCKsWX9rlSHBGY8VtUA2B2bXKSsZ9lO"}
END_POINT = "https://tequila-api.kiwi.com"
location_end_point = f"{END_POINT}/locations/query"


class FlightSearch:
    # THIS FUNCTION IS FOR GETTING IATA CODE FOR EACh CITY In OUR SHEET
    def get_flight_data(self, city):
        param = {
            "term":  city,
            "location_types": "city"
        }
        # WE ARE REQUESTING TO API TO GET IATA CODE THIS API RETURN DATA IN JSON FORMAT
        code = requests.get(url=location_end_point, params=param, headers=FLIGHT_SEARCH_API)
        code_data = code.json()["locations"]
        print(code_data)
        actual_code = code_data[0]["code"]
        return actual_code

    # THIS FUNCTION IS FOR PASSING ALL OUR DATA WHICH WE RETRIVED FROM ABOVE API REQUESTS
    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        param = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response_from_api = requests.get(url=f"{END_POINT}/v2/search", headers=FLIGHT_SEARCH_API,
                                         params=param)

        # IF IN CASE THERE IS NO FLIGHT TO OUR DESTINATION
        try:
            data_from_api = response_from_api.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        # THIS FUNCTION IS PASSING ALL DATA TO flight_data class to store data
        flight_data = FlightData(
            price=data_from_api["price"],
            origin_city=data_from_api["route"][0]["cityFrom"],
            origin_airport=data_from_api["route"][0]["flyFrom"],
            destination_city=data_from_api["route"][0]["cityTo"],
            destination_airport=data_from_api["route"][0]["flyTo"],
            out_date=data_from_api["route"][0]["local_departure"].split("T")[0],
            return_date=data_from_api["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ₹{flight_data.price}")
        return flight_data