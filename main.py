"""
    This file is part of simplecardgame.

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
from simplecardgame.classes.game import Game


def main():
    """Handles user input for simplecardgame."""
    continue_program = True
    is_new_game = True

    while continue_program:
        if is_new_game:
            user_respone = input("Would you like to play a game? [Y]es, [N]o ").upper()
            if user_respone == "Y":
                print(
                    "2 players play the game. They will draw 3 cards by taking turns.\n"
                    + "Whoever has the high score wins the game.\n"
                    + "Suit point number calculation: Clubs = 4, Hearts = 3, Diamonds = 2, Spades = 1.\n"
                    + "The winning value is calculated by suit point number * number on the card.\nYou are 'User'."
                )
                game = Game(2)
                game.play(is_new_game)
                is_new_game = False
            elif user_respone == "N":
                print("Have a nice day!")
                continue_program = False
        else:
            user_response = input("Would you like to play again? [Y]es, [N]o ").upper()
            if user_response == "Y":
                game.play(is_new_game)
            elif user_response == "N":
                print("Have a nice day!")
                continue_program = False


if __name__ == "__main__":
    main()
