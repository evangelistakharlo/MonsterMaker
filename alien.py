from monster import Monster

class Alien(Monster):
    def __init__(self):
        '''
        Constructor to initialize an Alien monster with default name and hp
        '''
        super().__init__(name="Alien", hp=10)
    
    def attack(self):
        '''
        Implements the abstract method attack() and returns the attack power of an alien
        Returns:
            (int): 4, attack power
        '''
        return 4