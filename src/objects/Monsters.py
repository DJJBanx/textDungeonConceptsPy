# Jackson Harding
# CS-172-A
# CS-172-60

# Imports
from src.objects.Monster import Monster, BASIC_HEALTH_BLOCK
from src.util.colors import Colors
import random

# Random Seed
# random.seed(1)

# Colors
cols = Colors()

# Disabled Colors
def disable():
    cols.disable(__name__)

# Ogre has 3 * BHB Health, 1 * BHB Attack, and defends 60% damage
# AI = 50% Chance to defend, 50% Chance to attack
class Ogre(Monster):
    def __init__(self):
        # Init with specific settings
        super(Ogre, self).__init__('Ogre', 3 * BASIC_HEALTH_BLOCK)

    # Basic attack with damage specified above
    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = BASIC_HEALTH_BLOCK
            print(cols.CYAN + 'The Ogre dealt '+cols.RED+str(damage)+' damage!')
            other.basicDefend(damage)

    # def advAttack(self, other):
    #     pass

    # Defense with percentage specified above
    def basicDefend(self, damage):
        if self.get_shield():
            damage = (damage * 4) // 10
            print(cols.CYAN + 'The Ogre blocked '+cols.LIGHT_CYAN+'60%'+cols.CYAN+' of the attack!')
            self.deShield()
        print(cols.CYAN + 'The Ogre was hit for', cols.RED+str(damage), 'damage!')
        self.add_health(-damage)

    # Generate random introduction.
    # Grant it, its only out of two options, but its still random
    def getSpeech(self):
        chance = random.randint(1, 2)
        if chance == 1:
            return 'U H - O H . . .'
        elif chance == 2:
            return 'H E L L O  L I T T L E  C R E A T U R E !'

    # The brain of the monster
    def basicAI(self, other):
        chance = random.randint(1, 10)
        if chance < 5:
            print(cols.CYAN + 'The Ogre hunkered down.')
            self.shield()
        else:
            self.basicAttack(other)

# I am not explaining the details of the rest of these but here are the summaries

# Spider has 3.5 * BHB Health, 1.5 * BHB Attack, and defends 20% damage
# AI = 30% Chance to defend, 70% Chance to attack
# Additional = unshielded attacks due 50% more damage.
class GiantSpider(Monster):
    def __init__(self):
        super(GiantSpider, self).__init__('Giant Spider', 3.5 * BASIC_HEALTH_BLOCK)

    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = 1.5 * BASIC_HEALTH_BLOCK
            print(cols.CYAN + 'The Spider dealt '+cols.RED+str(damage)+cols.CYAN+' damage!')
            other.basicDefend(damage)

    # def advAttack(self, other):
    #     pass

    def basicDefend(self, damage):
        if self.get_shield():
            damage = (damage * 8) // 10
            print(cols.CYAN + 'The Spider blocked '+cols.LIGHT_CYAN+'20%'+cols.CYAN+' of the attack!')
            self.deShield()
        else:
            print(cols.CYAN + 'The Spider wasn\'t defending! It is vunerable! It took '+cols.RED+'50%'+cols.CYAN+' more damage!')
            damage = (damage * 15) // 10
        print(cols.CYAN + 'The Spider was hit for', cols.RED+str(damage)+cols.CYAN, 'damage!')
        self.add_health(-damage)

    def getSpeech(self):
        chance = random.randint(1, 2)
        if chance == 1:
            return 'Hsssssssss...'
        elif chance == 2:
            return 'Sccrraaahhh!!! Krrrrttttt...'

    def basicAI(self, other):
        chance = random.randint(1, 10)
        if chance <= 3:
            print(cols.CYAN + 'The Spider protected itself!')
            self.shield()
        else:
            self.basicAttack(other)

# Troll has 5 * BHB Health, 0.75 * BHB Attack, and defends 66% damage
# AI = 70% Chance to defend, 30% Chance to attack
class Troll(Monster):
    def __init__(self):
        super(Troll, self).__init__('Troll', 5 * BASIC_HEALTH_BLOCK)

    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = 0.75 * BASIC_HEALTH_BLOCK
            print(cols.CYAN + 'The Troll dealt '+cols.RED+str(damage)+cols.CYAN+' damage!')
            other.basicDefend(damage)

    # def advAttack(self, other):
    #     pass

    def basicDefend(self, damage):
        if self.get_shield():
            damage = damage // 3
            print(cols.CYAN + 'The Troll blocked '+cols.LIGHT_CYAN+'66%'+cols.CYAN+' of the attack!')
            self.deShield()
        print(cols.CYAN + 'The Troll was hit for', cols.RED+str(damage)+cols.CYAN, 'damage!')
        self.add_health(-damage)

    def getSpeech(self):
        chance = random.randint(1, 2)
        if chance == 1:
            return 'Good luck getting by me bub!'
        elif chance == 2:
            return 'Another fruit to squash...'

    def basicAI(self, other):
        chance = random.randint(1, 10)
        if chance <= 7:
            print(cols.CYAN + 'The Troll gets in a defensive position.')
            self.shield()
        else:
            self.basicAttack(other)

# Knight has 4 * BHB Health, 12 * BHB Attack, and defends 75% damage
# AI = 40% Chance to defend, 40% Chance to attack, 20% to act cocky and do nothing
class Knight(Monster):
    def __init__(self):
        super(Knight, self).__init__('Knight', 4 * BASIC_HEALTH_BLOCK)

    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = 2 * BASIC_HEALTH_BLOCK
            print(cols.CYAN + 'The Knight dealt '+cols.RED+str(damage)+cols.CYAN+' damage!')
            other.basicDefend(damage)

    # def advAttack(self, other):
    #     pass

    def basicDefend(self, damage):
        if self.get_shield():
            damage = (damage * 25) // 100
            print(cols.CYAN + 'The Knight blocked '+cols.LIGHT_CYAN+'75%'+cols.CYAN+' of the attack!')
            self.deShield()
        print(cols.CYAN + 'The Knight was hit for', cols.RED+str(damage)+cols.CYAN, 'damage!')
        self.add_health(-damage)

    def getSpeech(self):
        chance = random.randint(1, 2)
        if chance == 1:
            return 'You do not deserve mercy.'
        elif chance == 2:
            return 'Pitiful. I deserve to fight a real champion.'

    def basicAI(self, other):
        chance = random.randint(1, 10)
        if self.get_shield():
            chance = random.randint(5, 10)
        if chance <= 4:
            print(cols.CYAN + 'The Knight raised his shield!')
            self.shield()
        elif chance <= 8:
            self.basicAttack(other)
        else:
            print(cols.LIGHT_RED + self.get_name() + ': ' + cols.CYAN + 'You don\'t deserve my attention...')

# Toadstool has 2 * BHB Health, 0.2 * BHB Attack, and defends 100% damage
# AI = 70% Chance to defend, 30% Chance to attack
class Toadstool(Monster):
    def __init__(self):
        super(Toadstool, self).__init__('Toadstool', 2 * BASIC_HEALTH_BLOCK)

    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = 0.2 * BASIC_HEALTH_BLOCK
            print(cols.CYAN + 'The Toadstool dealt '+cols.RED+str(damage)+cols.CYAN+' damage!')
            other.basicDefend(damage)

    # def advAttack(self, other):
    #     pass

    def basicDefend(self, damage):
        if self.get_shield():
            print(cols.CYAN + 'The Toad blocked '+cols.RED+'100%'+cols.CYAN+' of the attack!')
            self.deShield()
        else:
            print(cols.CYAN + 'The Toad was hit for', cols.RED+str(damage)+cols.CYAN, 'damage!')
            self.add_health(-damage)

    def getSpeech(self):
        chance = random.randint(1, 2)
        if chance == 1:
            return '*Boing* Hey there!'
        elif chance == 2:
            return 'Don\'t hurt me! I\'m squishy!'

    def basicAI(self, other):
        chance = random.randint(1, 10)
        if chance <= 7:
            print(cols.CYAN + 'The Toadstool starts sleeping.')
            self.shield()
        else:
            self.basicAttack(other)
