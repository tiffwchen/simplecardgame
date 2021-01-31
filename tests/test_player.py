"""
Tests the player module.
"""
import pytest
from simplecardgame.classes.player import Player
from simplecardgame.classes.deck import Deck
from simplecardgame.classes.suit import Suit


@pytest.fixture
def mock_player():
    """Creates an instance of the player class."""
    return Player("TestPlayer")


@pytest.fixture
def mock_deck():
    """Creates an instance of the deck class."""
    return Deck()


def test_player_name(mock_player):
    """Tests the player.name property."""
    assert mock_player.name == "TestPlayer"


def test_player_hand(mock_player):
    """Tests the player.hand property."""
    assert mock_player.hand == []


def test_player_score(mock_player):
    """Tests the player.score property."""
    assert mock_player.score == 0


def test_draw_card(mock_player, mock_deck, capsys):
    """Tests the player.draw_card() function."""
    mock_player.draw_card(mock_deck)
    mock_player.hand[0].show()
    captured = capsys.readouterr()
    assert len(mock_player.hand) == 1
    assert captured.out == "CLUB, 13\n"


def test_reset_hand_empty_hand(mock_player):
    """Tests the player.reset_hand() function on empty hand."""
    mock_player.reset_hand()
    assert len(mock_player.hand) == 0


def test_reset_hand_non_empty_hand(mock_player, mock_deck):
    """Tests the player.reset_hand() function on non-empty hand."""
    mock_player.draw_card(mock_deck)
    mock_player.reset_hand()
    assert len(mock_player.hand) == 0


def test_reset_score(mock_player):
    """Tests the player.reset_score() function."""
    mock_player.score = 2
    mock_player.reset_score()
    assert mock_player.score == 0


def test_calculate_score_empty_hand(mock_player):
    """Tests the player.calculate_score() function on empty hand."""
    mock_player.calculate_score()
    assert mock_player.score == 0


def test_calculate_score_non_empty_hand(mock_player, mock_deck):
    """Tests the player.calculate_score() function on non-empty hand."""
    mock_player.draw_card(mock_deck)
    mock_player.calculate_score()
    assert mock_player.score == 52


def test_show_hand_empty_hand(mock_player, capsys):
    """Tests the player.show_hand() function on empty hand."""
    mock_player.show_hand()
    captured = capsys.readouterr()
    assert captured.out == ""


def test_show_hand_non_empty_hand(mock_player, mock_deck, capsys):
    """Tests the player.show_hand() function on non-empty hand."""
    mock_player.draw_card(mock_deck)
    mock_player.draw_card(mock_deck)
    mock_player.show_hand()
    captured = capsys.readouterr()
    assert captured.out == "CLUB, 13\nCLUB, 12\n"


def test_sort_hand_non_empty_hand(mock_player, mock_deck):
    """Tests the player.sort_hand() function on non-empty hand."""
    mock_player.draw_card(mock_deck)
    mock_player.draw_card(mock_deck)
    assert mock_player.hand[0].suit == Suit.CLUB
    assert mock_player.hand[0].value == 13
    assert mock_player.hand[1].suit == Suit.CLUB
    assert mock_player.hand[1].value == 12
    mock_player.sort_hand()
    assert mock_player.hand[0].suit == Suit.CLUB
    assert mock_player.hand[0].value == 12
    assert mock_player.hand[1].suit == Suit.CLUB
    assert mock_player.hand[1].value == 13
