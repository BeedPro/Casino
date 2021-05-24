"""
Player Class 
	And inheritated Classes such as Passenger57 and Martingale
"""
import Errors
import Bet
import Outcome

class Player( object ):
	"""CLass for Player"""
	def __init__(self, table):
		self.stake = 200
		self.roundsToGo = 30
		self.table = table
		self.initalBet = 10
		self.nextBet = self.initalBet
  
	def reset(self):
		self.initalBet = 10
		self.nextBet = self.initalBet
		self.stake = 200
		self.roundsToGo = 30

	def playing(self):
		return (self.stake >= self.nextBet) and (self.roundsToGo != 0)

	def placeBets(self):
		if self.playing():
			self.newBet = Bet.Bet(self.nextBet, self.specificBet)
			try:
				self.table.placeBets(self.newBet)
			except (Errors.InvalidBet ) as errors:
				raise Errors.InvalidBet("Over Table Limit")

	def setStake(self, stake):
		self.stake = stake

	def setRounds(self, rounds):
		self.roundsToGo = rounds

	def winners(self, outcomes):
		pass

	def win(self, bet):
		amountWon = bet.winAmount()
		self.stake += amountWon
		print(f"Your Bet has Won: {amountWon}")

	def lose(self, bet):
		amountLost = bet.loseAmount()
		self.stake -= amountLost
		print(f"Your Bet has Lost: {amountLost}")
		
class Passenger57( Player ):
	def __init__(self, table, wheel):
		super().__init__(table)
		self.specificBet = Bet.Bet( 1, Outcome.Outcome("Black", 1))
		self.table = table
		self.wheel = wheel
  
	def placeBets(self):
		self.black = Outcome.Outcome("Black", 1)
		self.table.placeBets(Bet.Bet(1, self.black))

	def win(self, bet):
		super().win(bet)

	def lose(self, bet):
		super().lose(bet)
		
class Martingale( Player ):
	def __init__(self, table):
		super().__init__(table)
		self.lossCount = 0
		self.betMultiple = 1
		self.specificBet = table.wheel.getOutcome(Outcome.Outcome("Black", 1))

	def placeBets(self):
		self.nextBet = self.initalBet * self.betMultiple
		super().placeBets()

	def win(self, bet):
		super().win(bet)
		self.lossCount = 0
		self.betMultiple = 1
		

	def lose(self, bet):
		super().lose(bet)
		self.lossCount += 1
		self.betMultiple *= 2
		
	def reset(self):
		super().reset()
		self.lossCount = 0
		self.betMultiple = 1	

class SevenReds( Player ):
	def __init__(self, table):
		super().__init__(table)
		self.redCount = 7

	def placeBets(self):
		if self.redCount == 0:
			self.specificBet = self.table.wheel.getOutcome(Outcome.Outcome("Black", 1))
		return super().placeBets()

	def winners(self, outcomes):
		isRedOutcome = False
		for outcome in outcomes:
			if "Red" in outcome.name:
				self.redCount -= 1
				isRedOutcome = True
				break
		
		if not isRedOutcome:
			self.redCount = 7
		