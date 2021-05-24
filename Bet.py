"""
Bet Class
"""

class Bet( object ):
	"""Bet class to place a bet and see if player wins"""
	def __init__( self, amount, outcome):
		self.amount = amount
		self.outcome = outcome
	
	def winAmount( self ) -> int:
		return self.outcome.winAmount(self.amount)
	
	def loseAmount( self ) -> int:
		return self.amount

	def __str__( self ) -> str:
		return f"{self.amount} on {self.outcome}"
	
	def __repr__( self ) -> str:
		
		return f"{type(self).__name__}({vars(self)['amount']}, {vars(self)['outcome']})"