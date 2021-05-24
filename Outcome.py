"""
Outcome Class
"""


class Outcome(object):
    """ Each number has different outcomes with bets to win """
    def __init__(self, name, odds):
        self.name = str(name)
        self.odds = int(odds)

    def winAmount(self, amount):
        return self.odds * amount

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __ne__(self, other):
        if self.name != other.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} {self.odds}:1"

    def __repr__(self):
        return f"{type(self).__name__}({vars(self)['name']}, {vars(self)['odds']})"
