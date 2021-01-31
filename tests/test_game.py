"""
Tests the game module
"""
import pytest
from simplecardgame.classes.game import Game


@pytest.fixture
def mock_game():
    """Creates an instance of the game class."""
    return Game(2)


def test_game_deck(mock_game):
    """Tests the game.deck property."""
    assert mock_game.deck is not None
    assert len(mock_game.deck.cards) == 52


def test_game_player_count(mock_game):
    """Tests the game.player_count property."""
    assert mock_game.player_count == 2


def test_game_player(mock_game):
    """Tests the game.players property."""
    assert len(mock_game.players) == 2
    assert mock_game.players[0].name == "User"
    assert mock_game.players[1].name == "Computer 1"


def test_play_is_new_game(mock_game, capsys):
    """Tests the game.play() function."""
    mock_game.deck.show()
    original_deck_captured = capsys.readouterr()
    mock_game.play(True)
    winner_declaration_captured = capsys.readouterr()
    mock_game.deck.show()
    end_deck_captured = capsys.readouterr()
    expected_string_out = (
        "The winner is: " + mock_game.players[mock_game.player_count - 1].name + "\n"
    )
    assert original_deck_captured.out != end_deck_captured.out
    assert expected_string_out in winner_declaration_captured.out


def test_play_is_not_new_game(mock_game, capsys):
    """Tests the game.play() function."""
    mock_game.deck.show()
    original_deck_captured = capsys.readouterr()
    mock_game.play(False)
    winner_declaration_captured = capsys.readouterr()
    mock_game.deck.show()
    end_deck_captured = capsys.readouterr()
    expected_contained_string_out = (
        "The winner is: " + mock_game.players[mock_game.player_count - 1].name
    )
    assert original_deck_captured.out != end_deck_captured.out
    assert expected_contained_string_out in winner_declaration_captured.out


def test_play_not_enough_cards(mock_game, capsys):
    """Tests the game.play() function."""
    for __ in range(8):
        mock_game.play(False)
    mock_game.play(False)
    captured = capsys.readouterr()
    expected_contained_string_out_deck_renewal = "There are only 4 cards left. And we require 6 cards for the game. Deck has been renewed."
    expected_contained_string_out_winner = (
        "The winner is: " + mock_game.players[mock_game.player_count - 1].name
    )
    assert expected_contained_string_out_deck_renewal in captured.out
    assert expected_contained_string_out_winner in captured.out


def test_create_players(mock_game):
    """Tests the game.create_players() function."""
    orig_number_of_players = mock_game.player_count
    orig_player_array_length = len(mock_game.players)
    mock_game.player_count = 3
    mock_game.create_players()
    assert mock_game.player_count != orig_number_of_players
    assert len(mock_game.players) != orig_player_array_length
    assert mock_game.player_count == len(mock_game.players)


def test_shuffle_players(mock_game, capsys):
    """Tests the game.shuffle_players() function."""
    mock_game.shuffle_players()
    captured = capsys.readouterr()
    assert captured.out == mock_game.players[0].name + " goes first!\n"


def test_setup_game(mock_game, capsys):
    """Tests the game.setup_game() function."""
    mock_game.deck.show()
    pre_shuffled_deck_captured = capsys.readouterr()
    mock_game.setup_game()
    player_order_captured = capsys.readouterr()
    mock_game.deck.show()
    post_shuffled_deck_captured = capsys.readouterr()
    assert player_order_captured.out == mock_game.players[0].name + " goes first!\n"
    assert pre_shuffled_deck_captured.out != post_shuffled_deck_captured.out


def test_play_game(mock_game):
    """Tests the game.play_game() function."""
    mock_game.play_game()
    assert len(mock_game.players[0].hand) != 0
    assert len(mock_game.players[1].hand) != 0
    assert mock_game.players[0].score == 0
    assert mock_game.players[1].score == 0


def test_determine_winner(mock_game, capsys):
    """Tests the game.determine_winner() function."""
    mock_game.play_game()
    players_copy = mock_game.players
    for player in players_copy:
        player.calculate_score()
    players_copy = sorted(players_copy)
    mock_game.determine_winner()
    captured = capsys.readouterr()
    first_player_score_message = (
        mock_game.players[0].name + "'s score: " + str(mock_game.players[0].score)
    )
    second_player_scored_message = (
        mock_game.players[1].name + "'s score: " + str(mock_game.players[1].score)
    )
    assert players_copy[0] == mock_game.players[0]
    assert players_copy[1] == mock_game.players[1]
    assert first_player_score_message in captured.out
    assert second_player_scored_message in captured.out


def test_reset_player_hand(mock_game):
    """Tests the game.reset_player_hand() function."""
    mock_game.play_game()
    mock_game.determine_winner()
    assert len(mock_game.players[0].hand) != 0
    mock_game.reset_player_hand(mock_game.players[0])
    assert len(mock_game.players[0].hand) == 0


def test_reset_player_score(mock_game):
    """Tests the game.reset_player_score() function."""
    mock_game.play_game()
    mock_game.determine_winner()
    assert mock_game.players[0].score != 0
    mock_game.reset_player_score(mock_game.players[0])
    assert mock_game.players[0].score == 0


def test_reset_round(mock_game):
    """Tests the game.reset_round() function."""
    mock_game.play_game()
    mock_game.determine_winner()
    assert len(mock_game.players[0].hand) != 0
    assert len(mock_game.players[1].hand) != 0
    assert mock_game.players[0].score != 0
    assert mock_game.players[1].score != 0
    mock_game.reset_round()
    assert len(mock_game.players[0].hand) == 0
    assert len(mock_game.players[1].hand) == 0
    assert mock_game.players[0].score == 0
    assert mock_game.players[1].score == 0
