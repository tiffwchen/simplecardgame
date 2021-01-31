"""
Tests the card module.
"""

import pytest
from simplecardgame.classes.card import Card
from simplecardgame.classes.suit import Suit


@pytest.fixture
def mock_card():
    """Creates an instance of the card class."""
    return Card(Suit.SPADE, 1)


def test_card_suit(mock_card):
    """Tests the card.suit property."""
    assert mock_card.suit == Suit.SPADE


def test_card_value(mock_card):
    """Tests the card.value property."""
    assert mock_card.value == 1


def test_card_show(mock_card, capsys):
    """Tests the card.show() function."""
    mock_card.show()
    captured = capsys.readouterr()
    assert captured.out == "SPADE, 1\n"


def test_card_sort_ace_greater_than_king():
    """Tests that ace card is considered greater than king while sorting."""
    spade_ace_card = Card(Suit.SPADE, 1)
    spade_king_card = Card(Suit.SPADE, 13)
    assert spade_ace_card > spade_king_card


def test_card_suit_weights():
    """Tests that while sorting the suits from lowest to highest value are: Spade, Diamond, Heart, Club."""
    spade_ace_card = Card(Suit.SPADE, 1)
    diamond_ace_card = Card(Suit.DIAMOND, 1)
    heart_ace_card = Card(Suit.HEART, 1)
    club_ace_card = Card(Suit.CLUB, 1)
    assert spade_ace_card < diamond_ace_card
    assert diamond_ace_card < heart_ace_card
    assert heart_ace_card < club_ace_card
