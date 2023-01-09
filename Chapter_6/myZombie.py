import zombiedice,random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie2:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll
        rollornot = random.randint(0,1)
        while diceRollResults is not None:
            if rollornot == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie3:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombie4:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll
        val = random.randint(0,4)
        shotgunmm = 0
        while diceRollResults is not None and val != 0:
            shotgunmm += diceRollResults['shotgun']

            if shotgunmm < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break   
            val -= 1
class MyZombie5:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll
        shotgunz = 0
        brainsz = 0
        while diceRollResults is not None:
            shotgunz += diceRollResults['shotgun']
            brainsz += diceRollResults['brains']
            if shotgunz <= brainsz:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break



zombies = (
    MyZombie(name='Sarin'),
    MyZombie2(name='Chandra'),
    MyZombie3(name ='Ivin'),
    MyZombie5(name = 'Bob'),
    MyZombie4(name = 'Chad')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
