## Jamie Yates Python Coding for Euchre online- Hopeful Major Project!
## Step 1: Creating a Random Card Generator- Pull one item from two lists number and suit
import random
suit = [ "Spades", "Clubs", "Diamonds", "Hearts"]
facevalue = [ "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardvalue = random.randint(0, 12)
suitvalue = random.randint(0, 3)
##For Debugging purposes
##print cardvalue
##print suitvalue
print facevalue[cardvalue] + " of " + suit[suitvalue]
##Next step: Possibly create 4 Classes (one per player) In these create an array for hand, and variables for dealer and position at table
##Also create the dealing system- Loop to generate a random card, and check if it has already been given