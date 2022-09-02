import json
def get_local_price():
    with open("test_data.json") as test_data:
        test_dict = json.load(test_data)
        return test_dict["stations"]