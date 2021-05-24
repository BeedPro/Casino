"""
Simulator
"""

from Player import Player


class Simulator( object ):
    def __init__(self, player, game):
        self.initDuration = 30
        self.initStake = 200
        self.samples = 50
        self.maxima = []
        self.player = player
        self.game = game

    def session(self):
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
            maximas.append(max(stake))
            durations.append(len(stake))
        
        return (maximas, durations)