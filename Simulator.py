"""
Simulator
"""

from Player import Player
import math

class Simulator( object ):
    def __init__(self, player, game):
        self.initDuration = 250
        self.initStake = 1000
        self.samples = 50
        self.maxima = []
        self.player = player
        self.game = game

    def session(self):
        self.player.stake = self.initStake
        self.player.roundsToGo = self.samples
        self.player.initialBet = 10
        self.player.nextBet = 10
        stakeValues = []
        while self.player.playing():
            self.game.cycle(self.player)
            stakeValues.append(self.player.stake)
        
        self.player.reset() 

        return stakeValues

    def gather(self):
        stakes = []
        for _ in range(self.samples):
            stakes.append(self.session())
        
        maximas = []
        durations = []
        for stake in stakes:
            maximas.append(sorted(stake)[-1])
            durations.append(len(stake))
        
        return (maximas, durations)