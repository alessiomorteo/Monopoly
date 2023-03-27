from src.game_resources.monopoly_bank import MonopolyBank
import pytest

@pytest.fixture
def bank():
    return MonopolyBank()

def test_bank_initial_balance(bank):
    assert bank.get_bank_balance() == 25000

def test_bank_deposit(bank):
    bank.deposit(1000)
    assert bank.get_bank_balance() == 26000

def test_bank_withdraw(bank):
    bank.withdraw(1000)
    assert bank.get_bank_balance() == 24000

def test_bank_withdraw_insufficient_funds(bank):
    assert bank.withdraw(30000) == 0
    assert bank.get_bank_balance() == 25000

def test_bank_reset_balance(bank):
    bank.deposit(1000)
    bank.reset_bank_balance()
    assert bank.get_bank_balance() == 25000

def test_bank_str(bank):
    assert str(bank) == "Bank balance: 25000"
