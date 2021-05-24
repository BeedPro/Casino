"""
RouletteGame Class
"""
import Errors

class Game( object ):
    """Game CLass for the roulette game"""
    def __init__( self, wheel, table ):
        self.wheel = wheel
        self.table = table

        
    def cycle( self, player ):
        self.table.clearBets()
        player.placeBets()
        winBet = self.wheel.next()
        for bet in self.table.bets:
            winner = False
            for winningOutcome in winBet:
                if bet.outcome.name in winningOutcome.name:
                    winner = True
                    player.win(bet)
                    break
            if not winner:
                player.lose(bet)

        player.roundsToGo -= 1