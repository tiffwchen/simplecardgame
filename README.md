# simplecardgame 

An application to play a simple card game. 2 players play the game. They will draw 3 cards by taking turns. Whoever has the high score wins the game. Suit point number calculation are as follows: Clubs = 4, Hearts = 3, Diamonds = 2, Spades = 1. The winning value is calculated by suit point number * number on the card. Users are automatically designated as 'User'.

#### Set-up

1. Create the virtual environment.

            python -m venv c:\path\to\myenv

2. Activate virtual environment using one of the following commands (.bat for cmd, .ps1 for Powershell).

            .\myenv\Scripts\activate.bat
            .\myenv\Scripts\activate.ps1

2. Git clone the repository.

3. Install requirements.

            cd c:\path\to\simplecardgame
            pip install -r .\requirements.txt 

#### Running simplecardgame

1. Run the game using the following command:

            python c:\path\to\simplecardgame\main.py

#### Running Unit Tests

1. Run the unit tests from the root directory using:

            pytest c:\path\to\tests

#### Assumptions

1. No jokers in the deck.

2. Ace, Jack, King, Queen are 1, 11, 12, 13 in point evaluation, and they can be represented as such within the card object and while scoring.

3. "Draw three cards by taking turns" - one person draws 1 card, the other person draws 1 card, for 3 turns.

4. Due to the "if there is no card left in the deck, return error or exception" requirement for the function to get a card from the top of the deck, I'm assuming that it is allowed to play multiple games from the deck without recreating the deck every time.

5. The last element of a deck object's card array can be the "top of the deck" for the function to draw a card from the deck.  

6. Usage of random's shuffle function is allowed.

7. "Sort cards:  Sort cards in ascending order by suit and rank (ace high)" means that the sort will return, within a suit, "2,3,4,5,6,7,8,9,jack,queen,king,ace." Assumption that the sort will always happen in the order of suit values are evaluated when calculating points (spades=1, diamonds=2, hearts=3, clubs=4).

8. "card game which supports the all of the operations below" - assumption that this means that the logic of the game could handle all instances of shuffling, getting a card from the top of the deck, sorting the deck, and determining the winner without explicit user input.
