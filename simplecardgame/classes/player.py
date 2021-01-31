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
"""Class to represent player in simplecardgame.

    Typical usage example:

    player = Player()
    player.draw_card()
"""


class Player:

    """A player.

    Attributes:
        name: A string representing the player's name.
        hand: An array representing the cards in the player's hand.
        score: An integer count of the player's score.
    """

    def __init__(self, name):
        """Inits Player with name, hand, and score."""
        self.name = name
        self.hand = []
        self.score = 0

    def __eq__(self, other):
        """Defines when a player is equal to than another player."""
        return self.score == other.score

    def __lt__(self, other):
        """Defines when a player is less than another player."""
        return self.score < other.score

    def __gt__(self, other):
        """Defines when a player is greater than another player."""
        return self.score > other.score

    def draw_card(self, deck):
        """Draws a card from a deck of cards and add to player hand."""
        self.hand.append(deck.draw_card())

    def reset_hand(self):
        """Resets the player's hand to empty array."""
        self.hand = []

    def reset_score(self):
        """Resets the player's score to empty zero."""
        self.score = 0

    def calculate_score(self):
        """Shows the score of the player's hand."""
        for card in self.hand:
            self.score += card.suit.value * card.value

    def show_hand(self):
        """Shows the cards in player's hand."""
        for card in self.hand:
            card.show()

    def sort_hand(self):
        """Sorts the cards in player's hand."""
        self.hand = sorted(self.hand)
