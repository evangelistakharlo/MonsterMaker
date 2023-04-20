'''
    Name: 
    Date:
    Program description: A simple program that simmulates creating monsters and decorate them
'''

from check_input import get_int_range
from alien import Alien
from beast import Beast
from undead import Undead
from fire import Fire
from flying import Flying
from lasers import Lasers
from poison import Poison

print("Monster Maker")

# Get base monster choice
print("Choose base monster:")
print("1. Alien")
print("2. Beast")
print("3. Undead")
base_monster_choice = get_int_range(">>> ", 1, 3)

# Identify the base monster
my_monster = None
if base_monster_choice == 1:
    my_monster = Alien()
elif base_monster_choice == 2:
    my_monster = Beast()
elif base_monster_choice == 3:
    my_monster = Undead()

# Loop while not quitting
ability_choice  = -1
while ability_choice != 5:
    # Print monster info
    print(f"\n{my_monster}")

    print("Add an ability:")
    print("1. Fire")
    print("2. Flying")
    print("3. Lasers")
    print("4. Poison")
    print("5. Quit")
    ability_choice = get_int_range(">>> ", 1, 5)

    # Update monster by instantiating a decorator object
    if ability_choice == 1:
        my_monster = Fire(my_monster)
    elif ability_choice == 2:
        my_monster = Flying(my_monster)
    elif ability_choice == 3:
        my_monster = Lasers(my_monster)
    elif ability_choice == 4:
        my_monster = Poison(my_monster)

print(f"\nYour final monster is:\n{my_monster}")