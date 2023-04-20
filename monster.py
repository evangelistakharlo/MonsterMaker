from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name, hp):
        '''
        Constructor to initialize a monster with anme and hp
        Parameters:
            name (str): name of the monster
            hp (int): starting hp of the monster
        '''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        '''
        Getter property for name
        Returns:
            _name (str)
        '''
        return self._name
    
    @property
    def hp(self):
        '''
        Getter property for HP
        Returns:
            _hp (int)
        '''
        return self._hp
    
    @name.setter
    def name(self, name):
        '''
        Setter property for the name
        Parameters:
            name (str)
        '''
        self._name = name
    
    @hp.setter
    def hp(self, hp):
        '''
        Setter property for the HP
        Parameters:
            hp (int)
        '''
        self._hp = hp

    @abstractmethod
    def attack(self):
        '''
        Abstract method to get the attack power of a monster
        Returns:
            (int)
        '''
        pass
    
    def __str__(self) -> str:
        '''
        String representation of a Monster object
        Returns:
            (str): With name, hp, and attack power
        '''
        return f"Name: {self.name}\nHp: {self.hp}\nAttack: {self.attack()}"