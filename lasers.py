from decorator import Decorator
from monster import Monster

class Lasers(Decorator):
    def __init__(self, monst: Monster):
        '''
        Constructor to update the given monster with specific description
        Parameters:
            monst (Monster): monster to decorate
        '''
        monst.name = monst.name + " with lasers"
        monst.hp = monst.hp + 3
        super().__init__(monst)
    
    def attack(self):
        '''
        Returns the base attack power added by the bonus points
        '''
        return super().attack() + 4