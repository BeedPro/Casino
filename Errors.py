"""  
Error Classes
"""

class Error( Exception ):
	"""Base Error class for all errors"""
	pass

class InvalidBet( Error ):
	"""Error raised when bet is invalid"""
	def __init__( self, expr):
		self.expression = expr