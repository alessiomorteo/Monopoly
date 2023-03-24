from src.monopoly_player import MonopolyPlayer
from src.monopoly_property import MonopolyProperty
import pytest

@pytest.fixture()
def create_property():
    return MonopolyProperty("Mayfair", 400, 50)


def test_player_status():
    player = MonopolyPlayer("John", 1500)
    assert player.player_status() == {
        "player_name": "John",
        "balance": 1500,
        "properties": []
    }

def test_buy_property():
    player = MonopolyPlayer("John", 1500)
    property = create_property()
    player.buy_property(property)
    assert player.balance == 1100
    assert player.properties == [property]
    assert property.owner == player

def test_pay_rent():
    player1 = MonopolyPlayer("John", 1500)
    player2 = MonopolyPlayer("Jane", 1500)
    property = create_property()
    property.set_owner("Jane")
    player1.pay_rent(property, 50)
    assert player1.balance == 1450
    assert player2.balance == 1500

def test_can_afford():
    player = MonopolyPlayer("John", 250)
    assert player.can_afford(200) == True
    assert player.can_afford(300) == False
