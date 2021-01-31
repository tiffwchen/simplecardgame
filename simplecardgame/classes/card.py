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
"""Class to represent card in simplecardgame.

    Typical usage example:

    card = Card()
    card.show()
"""


class Card:

    """A card.

    Attributes:
        suit: An Enum representing the card's suit.
        value: An integer representing the card's value.
    """

    def __init__(self, suit, value):
        """Inits Card with suit and value."""
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        """Defines when a card is equal to than another card."""
        return self.suit == other.suit and self.value == other.value

    def __lt__(self, other):
        """Defines when a card is less than another card."""
        if self.suit == other.suit:
            self_value = self.value
            other_value = other.value

            if self.value == 1:
                self_value = 14
            if other.value == 1:
                other_value = 14
            return self_value < other_value
        else:
            return self.suit.value < other.suit.value

    def __gt__(self, other):
        """Defines when a card is greater than another card."""
        if self.suit == other.suit:
            self_value = self.value
            other_value = other.value

            if self.value == 1:
                self_value = 14
            if other.value == 1:
                other_value = 14
            return self_value > other_value
        else:
            return self.suit.value > other.suit.value

    def show(self):
        """Prints to console the card's suit and value."""
        print(self.suit.name + ", " + str(self.value))
