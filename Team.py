class Team
	##Class for a Team. Teams are made up of two players (1 and 3, or 2 and 4) Together through tricks/ rounds they then earn points
	
	def __init__(self, points):
		self.points = points
		self.Player = []