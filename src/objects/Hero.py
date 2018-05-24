# Jackson Harding
# CS-172-A
# CS-172-60

# Imports
from objects.Monster import Monster, BASIC_HEALTH_BLOCK
from util.colors import Colors

# Colors for this class
cols = Colors()


# Disable Colors
def disable():
    cols.disable(__name__)


# Hero Class
class Player(Monster):

    # Hero is a monster with potions and fireballs
    def __init__(self, name, potions=6, fireballs=10):
        super(Player, self).__init__(name, 7 * BASIC_HEALTH_BLOCK)
        self.__potions = potions
        self.__fireballs = fireballs

    # Return string representation of player items
    def get_items(self):
        return cols.BLUE + str(self.__fireballs) + ' Fireballs ' + cols.CYAN + '// ' + cols.BLUE + str(
            self.__potions) + ' Potions'

    # Sword attack that does
    # 1 * BasicHealthBlock
    def basicAttack(self, other):
        if isinstance(other, Monster):
            damage = BASIC_HEALTH_BLOCK
            other.basicDefend(damage)

    # Fireball attack does
    # 2 * BHB
    def advAttack(self, other):
        if isinstance(other, Monster):
            other.basicDefend(2 * BASIC_HEALTH_BLOCK)
            self.__fireballs -= 1

    # Defense protects against 50%
    def basicDefend(self, damage):
        if self.get_shield():
            damage = damage // 2
            print(cols.CYAN + 'You blocked ' + cols.LIGHT_CYAN + '50%' + cols.CYAN + ' of the attack!')
            self.deShield()
        print(cols.CYAN + 'You were hit for', cols.RED + str(damage), 'damage!')
        self.add_health(-damage)

    # Potion restores full health
    def usePotion(self):
        print(cols.CYAN + 'You used a potion!')
        if self.__potions > 0:
            self.set_health(self.get_health(0))
            self.__potions -= 1
