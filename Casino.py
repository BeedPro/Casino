"""
######################
#					 #  
#  CASINO SIMULATOR  #
#					 #
######################
"""

#### Importing Libaries and Classes
import BinBuilder
import Wheel
import Bet
import Bin
import Outcome
import Table
import RouletteGame
import Player
import Simulator

####
def main():
	# wheel = Wheel.Wheel()
	# bb = BinBuilder.BinBuilder()
	# bb.buildBins(wheel)
	# table = Table.Table(100, 1, wheel)
	# game = RouletteGame.Game(wheel, table)
	# player = Player.Martingale(table)
	# while player.playing():
	# 	game.cycle(player)
	# 	#print(player.stake)
	pass
	wheel = Wheel.Wheel()
	#bb = BinBuilder.BinBuilder()
	#bb.buildBins(wheel)
	table = Table.Table(100, 1, wheel)
	game = RouletteGame.Game(wheel, table)
	sim = Simulator.Simulator(Player.Martingale(table), game)
	maxima, duration = sim.gather()
	print(maxima, duration)

#### Main
if __name__ == "__main__":
    main() 
	### Tests 
    