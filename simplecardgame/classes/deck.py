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
from simplecardgame.classes.card import Card
from simplecardgame.classes.suit import Suit

"""Class to represent deck in simplecardgame.

    Typical usage example:

    deck = Deck()
    deck.draw_card()
"""


class Deck:

    """A deck

    Attributes:
        card: An array representing the cards in the deck.
    """

    def __init__(self):
        """Inits Deck with cards."""
        self.cards = []
        self.create_new_deck()

    def create_new_deck(self):
        """Creates and set a new array of cards as deck's cards attribute."""
        new_deck = []

        for enum in Suit:
            for val in range(1, 14):
                new_deck.append(Card(enum, val))

        self.cards = new_deck

    def draw_card(self):
        """Removes and returns the last card of cards."""
        try:
            return self.cards.pop()
        except Exception:
            print("No more cards in the deck. Card cannot be drawn.")

    def sort(self):
        """Sorts cards."""
        self.cards = sorted(self.cards)

    def shuffle_cards(self):
        """Shuffles cards."""
        shuffle(self.cards)

    def show(self):
        """Shows all cards."""
        for card in self.cards:
            card.show()
