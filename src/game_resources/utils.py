# General utils file for development
from monopoly_board import MonopolyBoard
from monopoly_property import MonopolyProperty
from monopoly_player import MonopolyPlayer
import json
from typing import List, Dict

def create_players(num_players: int, start_balance: int = 1500, player_names: List[str] = []) -> List[MonopolyPlayer]:
    """
    Creates a list of MonopolyPlayer objects.

    Args:
        num_players: The number of players to create.
        start_balance: The starting balance for each player. Defaults to 1500.
        player_names: A list of player names. If not provided, default names
            in the format "player_1", "player_2", etc. will be used.

    Returns:
        A list of MonopolyPlayer objects.
    """
    if num_players <= 0:
        raise ValueError("Number of players must be a positive integer.")
    
    if not player_names:
        player_names = [f"player_{i}" for i in range(1, num_players+1)]
    else:
        if len(player_names) != num_players:
            raise ValueError("Number of player names must match number of players.")
    
    return [MonopolyPlayer(name, start_balance) for name in player_names]

def flatten_and_order_json(file_path:str, key_label:str)->List[Dict]:
    """Function to import json and flatten into an ordered list, adding dictionary key to entry.

    Args:
        file_path (str): The path of the json to be flattened.
        key_label (str): A label to represent the keys of the json.

    Returns:
        List[Dict]: An ordered list of dictionary entries.
    """
    with open(file_path) as f:
        data = json.load(f)
    flat_data = []
    for key in data:
        for item in data[key]:
            item[key_label] = key
            flat_data.append(item)
    return sorted(flat_data, key=lambda x: x["id"])

def format_game_properties(game_properties: List[dict]) -> List[MonopolyProperty]:
    """
    Formats a list of game properties and returns a list of formatted properties.

    Args:
        game_properties (List[dict]): A list of game property dictionaries. Each dictionary
            should contain the following keys: "id", "name", "property_type", "price",
            "rent", "mortgage_value", "house_price", and "hotel_price".

    Returns:
        List[MonopolyProperty]: A list of formatted MonopolyProperty objects.
            If a property is a "rail_stations", "utilities", or "special" type, it will be
            formatted as None.

    """
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
    return formatted_game_properties


def setup_properties_from_json(file_path: str, key_label: str) -> List[MonopolyProperty]:
    """
    Sets up the Monopoly game properties from a JSON file.

    Args:
        file_path: The file path of the JSON file to load.
        key_label: The label to use for the keys in the flattened JSON data.

    Returns:
        A list of formatted MonopolyProperty objects. If a property is a "rail_stations",
        "utilities", or "special" type, it will be formatted as None.
    """
    sorted_properties = flatten_and_order_json(file_path, key_label)
    return format_game_properties(sorted_properties)

#prepared_properties = setup_properties_from_json("src/resources/monopoly_properties.json", "property_type")
#game_board = MonopolyBoard(prepared_properties)
#print(game_board.__str__)
