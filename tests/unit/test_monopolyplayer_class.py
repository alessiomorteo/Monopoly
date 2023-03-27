from src.game_resources.monopoly_property import MonopolyProperty
from src.game_resources.monopoly_bank import MonopolyBank
from src.game_resources.monopoly_player import MonopolyPlayer
import pytest

@pytest.fixture()
def sample_property():
    return MonopolyProperty("Mayfair", 300, 50)

@pytest.fixture()
def sample_player():
    return MonopolyPlayer("John", 500)

def test_player_status(sample_player: MonopolyPlayer):
    player = sample_player
    assert player.player_status() == {
        "player_name": "John",
        "balance": 500,
        "active_status": True,
        "jail_release_card": False
    }

def test_buy_property(sample_player: MonopolyPlayer, sample_property: MonopolyProperty):
    bank = MonopolyBank()
    sample_player.buy_property(bank, sample_property)
    assert sample_player.balance == 200
    assert sample_property.owner == "John"

def test_buy_property_insufficient_funds(sample_player: MonopolyPlayer, sample_property: MonopolyProperty):
    bank = MonopolyBank()
    sample_player.balance = 250
    assert not sample_player.buy_property(bank, sample_property)
    assert sample_player.balance == 250
    assert sample_property.owner is None

def test_pay_rent_sufficient_funds(sample_player: MonopolyPlayer, sample_property: MonopolyProperty):
    player1 = sample_player
    player2 = MonopolyPlayer("Not John", 1000)
    sample_property.set_owner(player2.name)
    assert player1.pay_rent(sample_property.rent)
    assert player1.balance == 450
    assert player2.balance == 1050

def test_pay_rent_insufficient_funds(sample_player: MonopolyPlayer, sample_property: MonopolyProperty):
    player1 = sample_player
    player1.balance = 0
    assert not player1.pay_rent(sample_property.rent)
    assert not player1.active

def test_receive_rent(sample_player: MonopolyPlayer):
    player1 = sample_player
    player2 = MonopolyPlayer("Not John", 1000)
    assert player1.receive_rent(50)
    assert player1.balance == 550
    assert player2.balance == 950

def test_credit_player(sample_player: MonopolyPlayer):
    player = sample_player
    assert player.credit_player(50)
    assert player.balance == 550

def test_credit_player_invalid_amount(sample_player: MonopolyPlayer):
    player = sample_player
    assert not player.credit_player(-50)
    assert player.balance == 500

def test_debit_player(sample_player: MonopolyPlayer):
    player = sample_player
    assert player.debit_player(50)
    assert player.balance == 450

def test_debit_player_invalid_amount(sample_player: MonopolyPlayer):
    player = sample_player
    assert not player.debit_player(-50)
    assert player.balance == 500

def test_can_afford_purchase(sample_player: MonopolyPlayer, sample_property: MonopolyProperty):
    player = sample_player
    property = sample_property
    assert player.can_afford_purchase(property.price)
    player.balance = 0
    assert not player.can_afford_purchase(property.price)

def test_receive_get_out_of_jail_card(sample_player: MonopolyPlayer):
    player = sample_player
    player.receive_get_out_of_jail_card()
    assert player.has_get_out_of_jail_card

def test_return_get_out_of_jail_card(sample_player: MonopolyPlayer):
    player = sample_player
    player.has_get_out_of_jail_card = True
    player.return_get_out_of_jail_card()
    assert not player.has_get_out_of_jail_card
