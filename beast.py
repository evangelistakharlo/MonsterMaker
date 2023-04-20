from monster import Monster

class Beast(Monster):
    def __init__(self):
        '''
        Constructor to initialize an Beast monster with default name and hp
        '''
        super().__init__(name="Beast", hp=10)
    
    def attack(self):
        '''
        Implements the abstract method attack() and returns the attack power of an beast
        Returns:
            (int): 5, attack power
        '''
        return 5