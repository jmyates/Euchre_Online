class Player:
	##Class for a Player. Contains variables for position at table and if they are the dealer, as well as their hand. (Attributes of class)
	
	def __init__(self, dealer, position):
		self.dealer = dealer
		self.position = position
		self.hand = []