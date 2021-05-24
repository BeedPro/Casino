"""
Table Class
"""
import Errors

class Table( object ):
	"""
	Table Class to see where the bets are placed
	"""

	def __init__( self, limit, minimum, wheel ):
		self.limit = limit 
		self.minimum = minimum
		self.bets = []
		self.wheel = wheel

	def placeBets( self, bet ):
		if self.isValid():
			self.bets.append(bet)
		else:
			raise Errors.InvalidBet(f"The Bet of {bet} exceeds limit of {self.limit}")

	def __iter__( self ):
		return self.bets[:].__iter__()

	def __str__( self ):
		return f"{self.bets}"

	def __repr__( self ):
		return f"{type(self).__name__}"
	
	def isValid( self ):
		if sum(obj.amount for obj in self.bets) > self.limit:
			return False
		return True

	def clearBets(self):
		self.bets.clear()