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
from enum import Enum


class Suit(Enum):
    """Enumeration to represent the four card suits.

    The suits have the values of Spade = 1,
    Diamond = 2, Heart = 3, Club = 4.

    Typical usage example:

    suit = Suit.SPADE
    suit_value = Suit.SPADE.value
    """

    SPADE = 1
    DIAMOND = 2
    HEART = 3
    CLUB = 4
