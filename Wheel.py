"""
Wheel Class
"""
### Importing libs, classes
import Bin
import random
import BinBuilder

###
class Wheel(object):
	"""A Wheel contains 38 bins, selection of a random Bin"""
	def __init__(self, rng=None):
		self.bins = list(Bin.Bin() for _ in range(38))
		self.rng = rng if rng is not None else random.Random()
		self.all_outcomes = set()
		self.rng.seed(4) # remove after stuff
		self.buildBins()

	def addOutcome(self, number, outcome):
		outcomes = list(self.bins[number])
		outcomes.append(outcome)
		self.all_outcomes.add(outcome)
		self.bins[number] = Bin.Bin(outcomes)

	def getOutcome(self, outcome):
		for oc in self.all_outcomes:
			if outcome.name in oc.name:
				return outcome

	def buildBins(self):
		bb = BinBuilder.BinBuilder()
		bb.buildBins(self)

	def next(self):
		rng_num = self.rng.randint(0,37)
		return self.bins[rng_num]
	
	def get(self, binN):
		return self.bins[binN]
###