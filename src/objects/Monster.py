# Jackson Harding
# CS-172-A
# CS-172-60

# Imports
from src.util.colors import Colors
import abc
import math

# The Basic Health Block that is used in all other
BASIC_HEALTH_BLOCK = 20

# Colors
cols = Colors()

class Monster:
    # Meta Class
    __metaclass__ = abc.ABCMeta

    # Init
    def __init__(self, name, health, drops=None):
        self.__name = name
        self.__healthf = health
        self.__health = health
        self.__charged = False
        self.__shielded = False

        # To be implemented later
        # self.__drops = []
        # if isinstance(drops, list):
        #     for i in drops:
        #         self.__drops.append(i)
        # elif drops:
        #     self.__drops.append(drops)

    # Something to help me
    def debug(self):
        return str([self.__name, self.__health, self.__drops])

    # @Override
    # public String toString() {
    #   return this
    # }
    def __str__(self):
        return cols.LIGHT_RED + self.__name + ': ' + cols.LIGHT_CYAN + self.getSpeech()

    # getters
    def get_name(self):
        return self.__name

    def get_health(self, f=1):
        return self.__healthf if f == 0 else self.__health

    def get_shield(self):
        return self.__shielded

    # Get Health Bar
    # This is pretty advanced and pretty cool
    def get_health_bar(self, size=10, color=None):
        hbtext = str(self.__health) + '/' + str(self.__healthf)
        spacer = ''
        for i in range(0, (size - (len(hbtext) - 1)) // 2):
            spacer += ' '
        hbtext = spacer + hbtext + spacer
        if len(hbtext) % 2 == 1:
            hbtext = hbtext[:len(hbtext) - 1]
        hs = math.ceil((self.__health / self.__healthf) * size)
        sh = ''
        if self.__shielded:
            sh += cols.BACKGROUND_CYAN + cols.BLACK + ' Shield '
        return cols.BACKGROUND_RED + hbtext[:hs] + cols.RESET + cols.BACKGROUND_LIGHT_BLACK + hbtext[hs:] + sh + cols.BACKGROUND_RESET + cols.RESET

    # To Be Implemented
    def get_drop(self, index=None):
        if isinstance(index, int):
            return self.__drops[index]
        else:
            return self.__drops

    # Setters
    def set_name(self, name):
        self.__name = name
        return self

    # Option to set healthf or health
    def set_health(self, health, f=0):
        if f == 1:
            self.__healthf = health
        else:
            self.__health = health
        return self

    # Health addition
    def add_health(self, health, f=0):
        if f == 1:
            self.__healthf += health
        else:
            self.__health += health
        return self

    # To be implemented {
    def add_drops(self, drops):
        if isinstance(drops, list):
            for i in drops:
                self.__drops.append(i)
        else:
            self.__drops.append(drops)
        return self

    def has_drop(self, drop):
        return drop in self.__drops

    def remove_drops(self, drops):
        if isinstance(drops, list):
            for i in drops:
                if i in self.__drops:
                    self.__drops.remove(i)
        else:
            if drops in self.__drops:
                self.__drops.remove(drops)
        return self
    # }

    # Shield On and Off
    def shield(self):
        self.__shielded = True

    def deShield(self):
        self.__shielded = False

    # To be implemented
    def charge(self):
        self.__charged = True


    # Abstract Methods
    @abc.abstractmethod
    def basicAttack(self, other):
        pass

    # To be implemented
    # @abc.abstractmethod
    # def advAttack(self, other):
    #     pass

    # More abstracts
    @abc.abstractmethod
    def basicDefend(self, damage):
        pass

    @abc.abstractmethod
    def basicAI(self):
        pass

    @abc.abstractmethod
    def getSpeech(self):
        pass

    # I have no idea why I need this here and not up there
    # but every time I placed it outside the Monster class
    # the entire game would crash sooooooooooooooooooo...
    # The only conclusion I have is that Python is an
    #                amazing language
    @classmethod
    def disable(cls):
        cols.disable(__name__)
