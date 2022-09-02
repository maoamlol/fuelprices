import requests

FUEL_TYPES = ["e5", "e10", "diesel", "all"]

with open("api_key.txt") as api_file:
    API_KEY = api_file.readline()
    if len(API_KEY) < 3:
        raise Exception("Invalid API KEY")

API_URL = "https://creativecommons.tankerkoenig.de/json/list.php"

def tankerkoenig_api_call(params):
    response = requests.get(url=API_URL, params=params)
    if response.status_code == 200:
        print("API CALLED!!!")
        return response.json()
    else:
        raise Exception(f"Error in response, got: {response.status_code}, message: {response.text}")


def get_prices(lat: float = 50.05798, lon: float = 8.24482, radius: float = 4, fuel_type: str = "all"):
    if radius < 0 or radius > 25:
        raise ValueError("radius has to be between 0 and 25")
    if fuel_type not in FUEL_TYPES:
        raise ValueError(f"fuel_type hast to be one of: {', '.join(FUEL_TYPES)}")
    if fuel_type == "all":
        sort_type = "dist"
    else:
        sort_type = "price"
    req_params = {
        "lat": lat,
        "lng": lon,
        "rad": radius,
        "sort": sort_type,
        "type": fuel_type,
        "apikey": API_KEY,
    }
    res_json = tankerkoenig_api_call(req_params)
    return res_json["stations"]

def get_example_data():
    example_params = {
        "lat": 50.05798,
        "lng": 8.24482,
        "rad": 4,
        "sort": "price",
        "type": "e10",
        "apikey": API_KEY,
    }
    return tankerkoenig_api_call(example_params)["stations"]

