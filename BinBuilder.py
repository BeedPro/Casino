"""
BinBuilder Class
"""
### Import lib, classes
import Outcome

### 
class BinBuilder:
	"""Create the Outcomes and add to Bin on Wheel"""
	def __init__(self):
		pass

	def buildBins(self, wheel):
		straight = self.straightBets()
		line = self.lineBets()
		street = self.streetBets()
		split = self.splitBets()
		corner = self.cornerBets()
		dozen = self.dozenBets()
		column = self.columnBets()
		evenMoney = self.evenMoneyBets()

		for bet in straight:
			n, outcome = bet
			wheel.addOutcome(n, outcome)

		for bet in line:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in street:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in split:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in corner:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in dozen:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in column:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		
		for bet in evenMoney:
			n, outcome = bet
			wheel.addOutcome(n, outcome)
		


	def straightBets(self):
		"""Bet on a single paying at 35:1"""
		outcomes = []
		outcomes.append((37, Outcome.Outcome("Straight 00", 35)))
		for i in range(37):
			outcomes.append((i, Outcome.Outcome(f"Striaght {i}", 35)))
		
		
		return outcomes

	def lineBets(self):
		"""Bet on Line bet paying at 5:1"""
		outcomes = []
		for r in range(0, 11, 1):
			n = 3*r + 1
			outcome = Outcome.Outcome(f"Line {n}-{n+1}-{n+2}-{n+3}-{n+4}-{n+5}", 5)
			for _ in range(6):
				outcomes.append((n, outcome))
				n += 1
		return outcomes

	def streetBets(self):
		"""Bet on Street bet paying at 11:1"""
		outcomes = []
		for r in range(0, 12, 1):
			n = 3*r + 1
			outcome = Outcome.Outcome(f"Street {n}-{n+1}-{n+2}", 11)
			
			for _ in range(3):
				outcomes.append((n, outcome))
				n += 1

		return outcomes
	
	def splitBets(self):
		"""Bet on Split bet paying at 17:1"""
		outcomes = []
		for r in range(0, 12, 1):
			n  = 3*r + 1
			outcome = Outcome.Outcome(f"Split {n}-{n+1}", 11)
			for _ in range(2):
				outcomes.append((n, outcome))
				n += 1
			n = 3*r + 2
			outcome = Outcome.Outcome(f"Split {n}-{n+1}", 11)
			for _ in range(2):
				outcomes.append((n, outcome))
				n += 1
			
		for r in range(0, 12, 1):
			n1 = 3*r + 1
			nums1 = [n1, n1+3]
			outcome = Outcome.Outcome(f"Split {n1}-{n1+3}", 11)
			for i in range(2):
				if n1 + 3 < 37:
					outcomes.append((nums1[i], outcome))	
			
			n2 = 3*r + 2
			nums2 = [n2, n2+3]
			outcome = Outcome.Outcome(f"Split {n2}-{n2+3}", 11)
			for i in range(2):
				if n2 + 3 < 37:
					outcomes.append((nums2[i], outcome))	

			n3 = 3*r + 3
			nums3 = [n3, n3+3]
			outcome = Outcome.Outcome(f"Split {n3}-{n3+3}", 11)
			for i in range(2):
				if n3 + 3 < 37:
					outcomes.append((nums3[i], outcome))	
				
		return outcomes

	def cornerBets(self):
		"""Creates the Corner bets outcome at odds of 8:1"""
		outcomes = []
		for r in range(0, 11, 1):
			n = 3*r + 1
			nums = [n, n+1, n+3, n+4]
			outcome = Outcome.Outcome(f"Corner {n}-{n+1}-{n+3}-{n+4}", 8)
			for i in range(4):
				outcomes.append((nums[i], outcome))
			
			n = 3*r  + 2
			nums = [n, n+1, n+3, n+4]
			outcome = Outcome.Outcome(f"Corner {n}-{n+1}-{n+3}-{n+4}", 8)
			for i in range(4):
				outcomes.append((nums[i], outcome))
		return outcomes

	def dozenBets(self):
		"""Creates Dozen Bets at odds of 2:1"""
		outcomes = []
		for d in range(0, 3, 1):
			dozenOutcome = Outcome.Outcome(f"Dozen {d+1}", 2)
				
			for m in range(0, 12, 1):
				outcomes.append(((12*d + m + 1), dozenOutcome))

		return outcomes

	def columnBets(self):
		"""Colum Bets with odds of 2:1"""
		outcomes = []
		for c in range(0, 3, 1):
			outcome = Outcome.Outcome(f"Column {c+1}", 2)
			for r in range(0 , 12, 1):
				outcomes.append((3*r+c+1, outcome))
		return outcomes

	def evenMoneyBets(self):
		"""Even Money bets with odds of 1:1"""
		outcomes = []
		redNumbers =  [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
		for n in range(1, 37, 1):
			### Low
			if n >= 1 and n < 19:
				outcomes.append((n, Outcome.Outcome(f"Low {n}", 1)))
				
			### High
			if n >= 19 and n < 37:
				outcomes.append((n, Outcome.Outcome(f"High {n}", 1))) 

			### Even 
			if n % 2 == 0:
				outcomes.append((n, Outcome.Outcome(f"Even {n}", 1)))
			
			### Odd
			if n % 2 == 1:
				outcomes.append((n, Outcome.Outcome(f"Odd {n}", 1)))
			
			### Red or Black
			if n in redNumbers:
				outcomes.append((n, Outcome.Outcome(f"Red {n}", 1)))
			else:
				outcomes.append((n, Outcome.Outcome(f"Black {n}", 1)))

		return outcomes
###