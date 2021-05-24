import random                               #used for randomising wheel spins (with or without a seed)

class Outcome:
    """
    Each number has a variety of Outcomes with bets that are 'winners'.
    Equality is important because there must be only one of each outcome i.e. ("Red" 1:1)
    To test this class, run test = Outcome("test",5) and then test.method() e.g. test.win_amount(5)
    Chapter 5, pages 37-43
    """
    def __init__(self, name, odds):         #each outcome must have a name and odds to be valid
        self.name = str(name)               #name can be numeric but is stored as a string for printing purposes
        self.odds = int(odds)               #odds are stored as an integer over one i.e. 8 means 8/1 (put 1, get 8)
  
    def winAmount(self, amount):            #how much would be won on this outcome, given an amount
        return self.odds * amount           #returns odds multiplied by amount staked

    def __eq__(self, other):                #are two names (strings) equal to one another?
        return self.name == other.name      #returns true if names match 

    def __ne__(self, other):                #are two names (strings) not equal to one another?
        return self.name != other.name      #returns true if names do not match

    def __hash__(self):                     #create the unique fixed length hashed value of name
        return hash(self.name)              #returns the hashed name with type integer
  
    def __str__(self):                      #prints out the name and odds for an outcome in format "name odds:1"
        return "{name:s} ({odds:d}:1)".format_map(vars(self))
	#vars is a dictionary of the attributes of an object, in this case (name and odds).
	#format_map will replace the dictionary indexes used in the string with those from the dictionary
  
    def __repr__(self):                     #prints out the values passed to the class when it was instantiated
        return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(self))
	#using ** here allows us to unpack a dictionary, that means instead of doing dict[0], dict[1]..etc..'
        #when called, this will look like: Outcome(name, odds) which is useful for checking that binbuilder has worked

class Bin(frozenset):                       #this is extending an existing data structure which means the class Bin is a frozenset
    """
    There are 38 bins (where the ball can land) on the roulette table, a bin is one of those 38 possible bins.
    Each bin will contain a collection of winning Outcomes for that bin. Set means unique values only. Frozen means fixed once created
    Each bin has between 12-14 individual Outcomes e.g. bin 1 will have a straight bet, split bet...etc
    Chapter 6, pages 45-48
    """
    pass                                    #class definition cannot be empty, currently there are no methods, pass is a placeholder

class Wheel:
    """
    A wheel will contain all 38 bins.
    The wheel will manage the bins and be able to randomly select one of these (0-37)
    Chapter 7, pages 49-52
    """
    def __init__(self):
        self.bins = list(Bin() for i in range(38))    #Create 38 bins in a list
        self.rng = random.Random()          #Storing an instance of the random library in self.rng (random number generator)
        self.rng.seed(4)                    #Using a starting seed to make the random predictable (15, 19, 6....)
        self.all_outcomes = set()           #Every single unique outcome stored in a set (unique only)
        bb = BinBuilder()                   #instantiate a binbuilder object
        bb.buildBins(self)                  #Build the bins using a method from binbuilder class
    
    def addOutcome(self, number, outcome):  #This method takes a outcome object and adds it to the bins on a wheel by number
        self.all_outcomes.add(outcome)      #Firstly add the outcome to the all_outcomes set
        self.bins[number] = Bin(self.bins[number] | Bin([outcome]))
        #Possibly the most complicated single line of code, it's responsible for generating each bin with all outcomes
        #In terms of how it works, the | sign is bitwise OR, this is essentially checking to see if the new outcome added...
        #...to the bin is already in the bins list, if it is then it doesn't add it again. If it isn't there then it recreates...
        #...the Bin and replaces the previous version
        
    def next(self):                         #Getter for the result of the next 'spin' of the wheel (one of 38 bins)
        return self.bins[self.rng.randint(0,37)]

    def get(self, bin):                     #Getter  for the contents of a specific bin
        return self.bins[bin]               #return the bin contents by index

    def getOutcome(self, outcomeName):
        for outcome in self.all_outcomes:
            if outcome.name == outcomeName:
                return outcome
    
class BinBuilder:
    """
    Creates all of the winning Outcomes and adds them to each bin on the wheel
    There are many types of bets that can be placed e.g. a street bet
    Each bin has 12-14 different ways that it can be a winner e.g. 1 can be straight, street, corner...
    This will create all of those potential outcomes and then create a bin out of them
    Chapter 8, pages 53-58
    """
    def buildBins(self, wheel):             #A method that will add all of the outcomes generated to a wheel
        outcomes = self.straightBets() + self.splitBets() + self.streetBets() + self.cornerBets()
        outcomes += self.lineBets() + self.dozenBets() + self.outsideBets()
        #Combine all of the returned lists from the bet types into one list
        for outcome in outcomes:            #Loop through the list looking at each outcome
            wheel.addOutcome(outcome[0],outcome[1])
            #Add the outcome to the wheel, taking the bin number first followed by the outcome itself
        
    def straightBets(self):
        """
        Bet on a single number paying at 35:1
        38 bets / 38 outcomes
        """ 
        outcomes = []                       #Empty list to store all of the possible bets
        for i in range(37):                 #Create the first 37 possible straight bets
            outcomes.append((i, Outcome(str(i), 35)))
            #store the outcome with the odds and bin number in the outcomes list
        outcomes.append((37,Outcome("00",35)))
        #Add the final outcome that can't be created in a list
        return outcomes                     #send the list of combinations back
  
    def splitBets(self):
        """
        Adjacent pair of numbers (column or row) paying at 17:1
        114 bets / 114 outcomes
        """
        outcomes = []
        plusone = list(range(1,35,3)) + list(range(2,36,3))
        plusthree = list(range(1,34))
        for i in plusone:
            string = "Split " + str(i) + "-" + str(i+1) 
            #n (original bin)
            outcomes.append((i,Outcome(string,17)))
            #n+1 (bin next to the original one)
            outcomes.append((i+1,Outcome(string,17)))
        for i in plusthree:
            string = "Split " + str(i) + "-" + str(i+3)
            #n (original bin)
            outcomes.append((i, Outcome(string,17)))
            #n+3 (bin underneath the original one)
            outcomes.append((i+3,Outcome(string,17)))
        return outcomes
  
    def streetBets(self):
        """
        3 numbers in a single row paying at 11:1
        12 possible bets / 36 outcomes
        """
        outcomes = []
        for i in range(1,35,3):
            string = "Street {}-{}-{}".format(i,i+1,i+2)
            for j in range(0,3):
                outcomes.append((i+j, Outcome(string,11)))
        return outcomes

    def lineBets(self):
        """
        A 6 number block (2 street bets) paying at 5:1
        11 possible bets
        """
        outcomes = []
        for i in range(1, 33, 3):
            string = 'Line {}-{}-{}-{}-{}-{}'.format(i, i + 1, i + 2, i + 3, i + 4, i + 5)
            for j in range(0, 6):
                outcomes.append((i+j, Outcome(string, 5)))
        return outcomes

    def dozenBets(self):
        """
        Each number is member of one of three dozens paying at 2:1
        3 possible bets
        """
        outcomes = []
        for i in [1,13,25]:
            string = 'Dozen {}-{}'.format(i, i+11)
            for j in range(0, 12):
                outcomes.append((i+j, Outcome(string, 2)))
        return outcomes

    def cornerBets(self):
        """
        Each number is member of one of three column paying at 2:1
        3 possible bets
        """
        outcomes = []
        for c in range(0, 3, 1):
            outcome = Outcome(f"Column {c+1}", 2)
            for r in range(0 , 12, 1):
                outcomes.append((3*r+c+1, outcome))
        return outcomes

    def outsideBets(self):
        reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        outcomes = []
        for i in range(1, 37):
            if i < 19:      #lower bets
                outcomes.append((i, Outcome("Low", 1)))
            else:           #higher bets
                outcomes.append((i, Outcome("High", 1)))
            if i % 2 == 0:  #even bet
                outcomes.append((i, Outcome("Even", 1)))
            else:           #odd bet
                outcomes.append((i, Outcome("Odd", 1)))
            if i in reds:   #red bet
                outcomes.append((i, Outcome("Red", 1)))
            else:           #black bet
                outcomes.append((i, Outcome("Black", 1)))
        return outcomes

class Bet():
    """
    A bet is the money/wager/stake placed on an Outcome
    Chapter 9, pages 59-63)
    """

    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome

    def winAmount(self):
        return self.outcome.winAmount(self.amount) #self.amount + 

    def loseAmount(self):
        return self.amount

    def __str__(self):
        return "{amount:d} on {outcome}".format_map(vars(self))

    def __repr__(self):
        return "{class_:s}({amount!r}, {outcome!r})".format(class_=type(self).__name__,**vars(self))

class Table:
    """
    A table is where bets can be placed
    Chapter 10, pages 63-68
    """
    def __init__(self, limit, minimum, wheel):
        self.limit = limit
        self.minimum = minimum
        self.bets = []
        self.wheel = wheel

    def placeBet(self, bet):
        self.bets.append(bet)           #is this the right placement?
        if not self.isValid(bet):
            raise InvalidBet(
                'The bet of {} exceeds table limit of {}'.format(
                    bet.amount, self.limit))
        #else maybe?

    def __iter__(self):
        return self.bets[:].__iter__()

    def __str__(self):
        pass

    def __repr__(self):
        pass
        
    def isValid(self,bet):                  #Checks whether the table limit has been reached
        if sum(obj.amount for obj in self.bets) > self.limit:
            #returns false if the sum of all subjects is greater than the limit for the table
            return False
        return True                         #returns True to otherwise

    def clearBets(self):
        self.bets.clear()

class InvalidBet(Exception):
    """
    InvalidBet is raised when a player attempts to place a bet exceeding limits
    Chapter 10, pages 66-67
    """
    def __init__(self, expression):
        self.expression = expression

class RouletteGame():
    """
    This class manages the game state through the cycle method
    Chapter 11, pages 71-73
    """
    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        self.table.clearBets()
        player.placeBets()
        winning_bin = self.table.wheel.next()       #spinning the wheel/get winner
        for betmade in self.table.bets:             #loop through all bets
            winner = False
            for winning_outcome in winning_bin:
                if betmade.outcome.name == winning_outcome.name:
                    winner = True
                    player.win(betmade)
                    break
            if winner == False:
                player.lose(betmade)

        player.roundsToGo -= 1
        
class Player():
    """
    This is a superclass where players specialise from (inherited)
    Chapter 13, pages 79-84)
    """
    def __init__(self, table):
        self.stake = 200
        self.roundsToGo = 30
        self.table = table
        self.initialBet = 10
        self.nextBet = self.initialBet

    def isPlaying(self):
        return (self.stake >= self.nextBet) and (self.roundsToGo != 0)

    def win(self, bet):
        amountWon = bet.winAmount()
        self.stake += amountWon

    def lose(self, bet):
        amountLost = bet.loseAmount()
        self.stake -= amountLost
    
    def placeBets(self):
        if self.isPlaying():
            self.newBet = Bet(self.nextBet, self.specificBet)
            try:
                self.table.placeBet(self.newBet)
            except (InvalidBet) as error:
                raise InvalidBet('Over table limit')

class Passenger57(Player):
    """
    Player who always bets on black
    Not a real strategy, simply for testing
    Chapter 11, pages 69-73
    """
    def __init__(self, table, wheel):
        super().__init__(table)
        self.wheel = wheel
        self.table = table
        self.specificBet = table.wheel.getOutcome("Black")

    def placeBets(self):
        self.black = Outcome("Black", 1)
        self.table.placeBet(Bet(1, self.black))

    def win(self, bet):
        super().win(bet)
        print("Your bet has won: {}".format(bet.winAmount()), player.stake)

    def lose(self, bet):
        super().lose(bet)
        print("Your bet was a loser", player.stake)            

wheel = Wheel()
table = Table(100, 1, wheel)
game = RouletteGame(wheel, table)
player = Passenger57(table,wheel)
while player.isPlaying():
    game.cycle(player)