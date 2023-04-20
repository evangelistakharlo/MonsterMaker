from monster import Monster

class Undead(Monster):
    def __init__(self):
        '''
        Constructor to initialize an Undead monster with default name and hp
        '''
        super().__init__(name="Undead", hp=10)
    
    def attack(self):
        '''
        Implements the abstract method attack() and returns the attack power of an unedad
        Returns:
            (int): 3, attack power
        '''
        return 3