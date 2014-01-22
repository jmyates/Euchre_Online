##Start of my main program Euchre Online. CSH Jamie Yates
from Player import Player
import random ##To allow for random selection of cards in deal
##Creating the four individual players
player1 = Player(True, 1)
player2 = Player(False, 2)
player3 = Player(False, 3)
player4 = Player(False, 4)

from Team import Team
team1 = [player1, player3]
team2 = [player2, player4]

##Creating the Deck of Cards (9 through Ace)
