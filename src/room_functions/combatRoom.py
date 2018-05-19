# Jackson Harding
# CS-172-A
# CS-172-60

# Add Directory /objects to system path
import sys

# Imports
from src.objects import Hero, Monsters, Monster
from src.objects.Monsters import *
from src.util.colors import Colors
import random
import time
import math

# Colors constant
cols = Colors()

def disable():
    cols.disable(__name__)

#################
# Game Settings
#################

# Introduce ASCII Escape Values
print('This python script uses ASCII Escape Codes.')
print(
    cols.RED + 'This text should be red! If you see a question mark and numbers at the beginning/end of this sentence that is bad.' + cols.RESET)
checking = True
while checking:
    # Check to see if their console can use them
    ans = input('Are you using a console that supports these? (Yes or No)\n')
    if ans.lower()[:3] == 'yes':
        checking = False
    elif ans.lower()[:2] == 'no':
        # If the user can't use these values then disable all of them
        Hero.disable()
        Monsters.disable()
        Monster.disable()
        disable()
        checking = False
    else:
        # It is important
        print('Please put in a valid response, this is an important setting for the game.')

# Time setting for the game
# The game has sections that are time delayed for dramatic effect
timeManagement = 0
checking = True
while checking:
    print('Do you want artistic delays?')
    # This is how you delay in python
    time.sleep(1)
    print('(Yes or No)')
    time.sleep(1)
    ans = input('(Like that ^)\n')
    if ans.lower()[:3] == 'yes':
        # Time delay enabled
        timeManagement = 1
        checking = False
    elif ans.lower()[:2] == 'no':
        # Time delay disabled
        timeManagement = 0
        checking = False
    else:
        print('Please put in a valid response, this is an important setting for the game.')

#############
# Game Setup
#############

# Introductions
print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Welcome to the coliseum!')

# Get Name
name = input(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'What is your name, champion?\n')
print(cols.RED + 'King Mythryl: ' + cols.BLUE + name + cols.YELLOW + '... What a pitiful name... HAHA!')

# Seed for inputs
# random.seed(1)

# Select amount of enemies
amount = 0
selecting = True
while selecting:
    tmp = input(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'How many enemies do you wish to battle?\n' + cols.RED +
                'King Mythryl: ' + cols.YELLOW + 'I will give you ' + cols.BLUE + '1 potion ' + cols.YELLOW + 'for every 3 enemies'
                                                                                                              ' and ' + cols.BLUE + '1 fireball' + cols.YELLOW + ' for every 2 enemies!\n')
    try:
        amount = int(tmp)
        if amount < 1:
            raise ValueError
        selecting = False
    except ValueError:
        # presetOverride is a predetermined group of monsters used in input2.txt, it is the most balanced example of gameplay with the most diversity
        if tmp == 'presetOverride':
            amount = -37
            print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'As you wish my liege')
            break;
        print(cols.RED + 'King Mythryl: ' + cols.YELLOW + tmp + '?! What on earth on you going on about?')
        print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Let\'s try again... Give me an integer.')

# Array of enemies
enemies = []

# Random assignment of monsters
for i in range(0, amount):
    chance = random.randint(1, 5)
    if chance == 1:
        enemies.append(Ogre())
    elif chance == 2:
        enemies.append(Troll())
    elif chance == 3:
        enemies.append(Knight())
    elif chance == 4:
        enemies.append(Toadstool())
    elif chance == 5:
        enemies.append(GiantSpider())

# presetOverride
if amount == -37:
    enemies = [Ogre(), Knight(), GiantSpider(), Troll(), Toadstool(), Ogre()]
    amount = 6

# Player object
player = Hero.Player(name, math.ceil(len(enemies) / 3), math.ceil(len(enemies) / 2))

# Intro to gameplay
print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Well... Then let us begin...')
print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'First up...')

###########
# Gameplay
###########

# Gameloop
for i, e in enumerate(enemies):
    # Enemy number
    print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Fighter number ' + str(i + 1) + '! HAHAHA!')
    print(e)

    # Fighting loop
    fighting = True
    while fighting:
        # Print Enemy and Player health
        print()
        print(cols.BLUE + name + ': ' + player.get_health_bar())
        print(cols.CYAN + 'VS')
        print(cols.LIGHT_RED + e.get_name() + ': ' + e.get_health_bar())
        print()

        # Player Stats
        print(cols.CYAN + 'Your turn!')
        print(cols.CYAN + 'Remaining items: ' + player.get_items())
        inp = input(cols.CYAN + 'Enter Command: ' + cols.MAGENTA + '(Sw)ord (Sh)ield (F)ireball (P)otion (Exit)\n')

        # Check for input == None
        if len(inp.lower()) < 1:
            inp = 'Failed'

        # Check for valid commands
        if inp.lower()[:2] == 'sw':
            # Sword
            player.basicAttack(e)
        elif inp.lower()[:2] == 'sh':
            # Shield
            print(cols.CYAN + 'You shielded up!')
            player.shield()
        elif inp.lower()[0] == 'f':
            # Fireball
            player.advAttack(e)
        elif inp.lower()[0] == 'p':
            # Potion
            player.usePotion()
        elif inp.lower() == 'exit':
            # Exit
            print('Thanks for playing!')
            sys.exit()
        else:
            # Invalid Input
            print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'You imbecile! That\'s not a valid input!')
            continue

        # If enemy is dead then its dead
        if e.get_health() <= 0:
            # Some funny comments and then end fighting and continue
            print(cols.CYAN + 'The ' + cols.RED + e.get_name() + cols.CYAN + ' died!')
            time.sleep(1 * timeManagement)
            print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Hmmm... NEXT OPPONENT!')
            time.sleep(2 * timeManagement)
            fighting = False
            continue

        # Print health and stats for enemy
        print()
        print(cols.BLUE + name + ': ' + player.get_health_bar())
        print(cols.CYAN + 'VS')
        print(cols.LIGHT_RED + e.get_name() + ': ' + e.get_health_bar())
        print()
        print(cols.LIGHT_RED + e.get_name() + '\'s ' + cols.CYAN + 'turn!')

        # Enemy decision
        print('Awaiting command...')
        # Simulate the enemy thinking
        time.sleep(1.5 * timeManagement)
        # Make decision
        e.basicAI(player)
        # Give player time to read
        time.sleep(2.25 * timeManagement)
        # If player died then kill him
        if player.get_health() <= 0:
            print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'HAHAHA! I guess you fail...')
            print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Until next time...')
            sys.exit(0)

# Funny ending with time delay
time.sleep(1 * timeManagement)
print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'WHAT?!?! There is no one left?!')
time.sleep(1 * timeManagement)
print(cols.RED + 'King Mythryl: ' + cols.YELLOW + 'Fine... I\'ll do it myself...')
time.sleep(3 * timeManagement)

# the Reality
print(cols.RESET + 'jk, I am too lazy to implement a full scale boss battle. :P Thanks for playing!')

# I wish I could've done a boss battle but I didn't have time.