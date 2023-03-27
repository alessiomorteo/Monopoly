
import pytest
from src.game_resources.monopoly_board import MonopolyBoard
from src.game_resources.monopoly_property import MonopolyProperty
from src.game_resources.monopoly_card_deck import CardDeck
from typing import List

class TestMonopolyBoard:

    @pytest.fixture
    def board(self):
        return MonopolyBoard([])

    @pytest.fixture
    def prop1(self):
        return MonopolyProperty("Mayfair", 400, 50)

    @pytest.fixture
    def prop2(self):
        return MonopolyProperty("Park Place", 350, 45)

    def test_add_property(self, board, prop1):
        board.add_property(prop1)
        assert board.properties == [prop1]

    def test_get_property(self, board, prop1, prop2):
        board.add_property(prop1)
        board.add_property(prop2)
        assert board.get_property("Mayfair") == prop1
        assert board.get_property("Park Place") == prop2
        assert board.get_property("Invalid Name") is None

    def test_add_chance(self, board):
        board.add_chance("Advance to Go")
        assert board.chance_cards == ["Advance to Go"]

    def test_add_community_chest(self, board):
        board.add_community_chest("Bank error in your favor")
        assert board.community_chest_cards == ["Bank error in your favor"]

    def test_pick_card(self, board):
        with pytest.raises(ValueError):
            board.pick_card("Invalid Type")
        
        board.add_chance("Advance to Go")
        board.add_chance("Go to Jail")
        
        assert board.pick_card("chance") == "Go to Jail"

        board.add_community_chest("Bank error in your favor")
        board.add_community_chest("Collect $50")
        assert board.pick_card("community_chest") == "Collect $50"
