from src.game_resources.monopoly_player import MonopolyPlayer
from src.game_resources.monopoly_property import MonopolyProperty
import pytest

@pytest.fixture()
def sample_property():
    return MonopolyProperty("Mayfair", 400, 50)

def test_player_status():
    player = MonopolyPlayer("John", 1500)
    assert player.player_status() == {
        "player_name": "John",
        "balance": 1500,
        "properties": []
    }

def test_buy_property(sample_property):
    player = MonopolyPlayer("John", 1500)
    property = sample_property
    player.buy_property(property)
    assert player.balance == 1100
    assert player.properties == [property]
    assert property.owner == player

def test_pay_rent(sample_property):
    player1 = MonopolyPlayer("John", 1500)
    sample_property.set_owner("John")
    player1.pay_rent(sample_property.rent)
    assert player1.balance == 1450

def test_receive_rent(sample_property):
    player1 = MonopolyPlayer("John", 1500)
    sample_property.set_owner("John")
    player1.receive_rent(sample_property.rent)
    assert player1.balance == 1550

def test_can_afford():
    player = MonopolyPlayer("John", 250)
    assert player.can_afford(200) == True
    assert player.can_afford(250) == True
    assert player.can_afford(251) == False
    assert player.can_afford(300) == False
