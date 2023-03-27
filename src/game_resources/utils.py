# General utils file for development
from monopoly_board import MonopolyBoard
from monopoly_property import MonopolyProperty
import json

def flatten_and_order_json(file_path:str, key_label:str)->list:
    """Function to import json and flatten into an ordered list, adding dictionary key to entry.

    Args:
        file_path (str): The path of the json to be flattened.
        key_label (str): A label to represent the keys of the json.

    Returns:
        list: An ordered list of dictionary entries.
    """
    with open(file_path) as f:
        data = json.load(f)
        flat_data = []
        for key in data:
            for item in data[key]:
                item[key_label] = key
                flat_data.append(item)
        return sorted(flat_data, key=lambda x: x["id"])

game_properties = flatten_and_order_json("src/resources/monopoly_properties.json", "property_type")
formatted_game_properties = []
for property_i in game_properties:
    property_type = property_i.pop("property_type")
    property_i["position"] = property_i.pop("id")
    if property_type == "regular":
        property_i.pop("house_price")
        property_i.pop("hotel_price")
        formatted_property = MonopolyProperty(**property_i)
    elif property_type == "rail_stations":
        formatted_property = None
    elif property_type == "utilities":
        formatted_property = None
    elif property_type == "special":
        formatted_property = None
    else:
        formatted_property = MonopolyProperty(**property_i)
        #raise ValueError()
    formatted_game_properties.append(formatted_property)

game_board = MonopolyBoard(properties=formatted_game_properties)

print(game_board.__str__)
