"""
Tests the deck module.
"""
import pytest
from simplecardgame.classes.deck import Deck


@pytest.fixture
def mock_deck():
    """Creates an instance of the deck class."""
    return Deck()


def test_deck_cards(mock_deck):
    """Tests the deck.cards property."""
    assert len(mock_deck.cards) == 52


def test_create_new_deck(mock_deck):
    """Tests the deck.create_new_deck() function."""
    mock_deck.draw_card()
    assert len(mock_deck.cards) == 51
    mock_deck.create_new_deck()
    assert len(mock_deck.cards) == 52


def test_draw_card_non_empty_deck(mock_deck):
    """Tests the deck.draw_card() function on non-empty deck."""
    assert len(mock_deck.cards) == 52
    mock_deck.draw_card()
    assert len(mock_deck.cards) == 51


def test_draw_card_empty_deck(mock_deck, capsys):
    """Tests the deck.draw_card() function on empty deck."""
    deck_length = len(mock_deck.cards)
    i = 0
    while i < deck_length + 1:
        mock_deck.draw_card()
        i += 1
    captured = capsys.readouterr()
    assert captured.out == "No more cards in the deck. Card cannot be drawn.\n"


def test_sort(mock_deck, capsys):
    """Tests the deck.sort() function."""
    mock_deck.shuffle_cards()
    mock_deck.show()
    shuffle_deck_captured = capsys.readouterr()
    mock_deck.sort()
    mock_deck.show()
    sorted_deck_captured = capsys.readouterr()
    assert shuffle_deck_captured.out != sorted_deck_captured.out


def test_shuffle_cards(mock_deck, capsys):
    """Tests the deck.shuffle_cards() function."""
    mock_deck.show()
    original_deck_captured = capsys.readouterr()
    mock_deck.shuffle_cards()
    mock_deck.show()
    shuffle_deck_captured = capsys.readouterr()
    assert original_deck_captured.out != shuffle_deck_captured.out


def test_show(mock_deck, capsys):
    """Tests the deck.show() function."""
    deck_length = len(mock_deck.cards)
    i = 0
    while i < deck_length - 1:
        mock_deck.draw_card()
        i += 1
    mock_deck.show()
    captured = capsys.readouterr()
    assert captured.out == "SPADE, 1\n"
