"""This file is part of simplecardgame.

    simplecardgame is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    simplecardgame is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with simplecardgame.  If not, see <https://www.gnu.org/licenses/>.
"""
from random import shuffle
from simplecardgame.classes.deck import Deck
from simplecardgame.classes.player import Player

"""Class to represent game in simplecardgame.

    Typical usage example:

    game = Game()
    deck.play()
"""


class Game:

    """A game

    Attributes:
        deck: An instance of deck.
        player_count: An integer representing the number of players.
        players: An array for storing the instances of player.
    """

    def __init__(self, player_count=2):
        """Inits game with deck and players."""
        self.deck = Deck()
        self.player_count = player_count
        self.players = []
        self.create_players()

    def play(self, is_new_game):
        """Plays the game, handling game logic."""
        if is_new_game:
            self.setup_game()
        else:
            self.reset_round()

            min_required_cards = 3 * self.player_count
            if len(self.deck.cards) < min_required_cards:
                print(
                    "There are only "
                    + str(len(self.deck.cards))
                    + " cards left. And we require "
                    + str(min_required_cards)
                    + " cards for the game. Deck has been renewed."
                )
                self.deck.create_new_deck()
                self.deck.shuffle_cards()

        self.play_game()
        print("The winner is: " + self.determine_winner().name)

    def create_players(self):
        """Creates new player array and appends new players to it."""
        players = []
        players.append(Player("User"))
        for i in range(1, self.player_count):
            player_name = "Computer " + str(i)
            players.append(Player(player_name))

        self.players = players

    def shuffle_players(self):
        """Shuffles the players."""
        shuffle(self.players)
        print(self.players[0].name + " goes first!")

    def setup_game(self):
        """Sets up the game by shuffling the deck and players."""
        self.deck.shuffle_cards()
        self.shuffle_players()

    def play_game(self):
        """Plays the game by drawing 3 cards for each player, taking turns."""
        for __ in range(3):
            for player in self.players:
                player.draw_card(self.deck)
                player.sort_hand()
                print(player.name + "'s hand:")
                player.show_hand()

    def determine_winner(self):
        """Calculates the score and determines the winning player."""
        for player in self.players:
            player.calculate_score()
        self.players = sorted(self.players)
        for player in self.players:
            print(player.name + "'s score: " + str(player.score))
        return self.players[len(self.players) - 1]

    def reset_player_hand(self, player):
        """Resets player hand."""
        player.reset_hand()

    def reset_player_score(self, player):
        """Resets player score."""
        player.reset_score()

    def reset_round(self):
        """Resets the round: shuffling deck and resetting hands and score of players."""
        self.deck.shuffle_cards()
        for player in self.players:
            self.reset_player_hand(player)
            self.reset_player_score(player)
        self.shuffle_players()
