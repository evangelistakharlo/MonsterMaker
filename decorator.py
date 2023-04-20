from abc import ABC
from monster import Monster

class Decorator(Monster, ABC):
    def __init__(self, monst):
        '''
        Constructor to initialize its Monster object
        Parameters:
            monst (Monster): Monster to decorate
        '''
        self._monster = monst
        super().__init__(monst.name, monst.hp)
        
    def attack(self):
        '''
        Implements the abstract attack() method and returns the
        current attack power of monster ity is decorating
        Returns:
            (int)
        '''
        return self._monster.attack()