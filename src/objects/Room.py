from util.colors import Colors
import abc
import random

cols = Colors()

def disable():
    cols.disable(__name__)

# init(autoreset=True)
ids = [
    cols.YELLOW + 'Wood' + cols.LIGHT_YELLOW,
    cols.LIGHT_BLACK + 'Stone' + cols.LIGHT_YELLOW,
    cols.RED + 'Lava' + cols.LIGHT_YELLOW,
    cols.LIGHT_MAGENTA + 'Marble' + cols.LIGHT_YELLOW,
    cols.BLUE + 'Granite' + cols.LIGHT_YELLOW,
    cols.LIGHT_CYAN + 'Mossy Cobblestone' + cols.LIGHT_YELLOW,
    cols.CYAN + 'Glass' + cols.LIGHT_YELLOW,
    cols.LIGHT_RED + 'Drywall' + cols.LIGHT_YELLOW,
    cols.LIGHT_BLUE + 'Tiled' + cols.LIGHT_YELLOW,
    cols.LIGHT_GREEN + 'Chalkboards' + cols.LIGHT_YELLOW
]


class Room(metaclass=abc.ABCMeta):
    # Constructor sets the description
    # All four doors should be set to None to start
    def __init__(self, descr, type=0, identifiers=None):
        # Description of the room to print out
        # These should be unique so the player knows where they are
        if not identifiers:
            self.identifiers = [ids[random.randint(0, len(ids) - 1)], ids[random.randint(0, len(ids) - 1)],
                                ids[random.randint(0, len(ids) - 1)]]
        else:
            self.identifiers = identifiers
        self.__descr = descr
        # These either tell us what room we get to if we go through the door
        # or they are None if the "door" can't be taken.
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None

        self.__type = type

    # Access
    # Return the correct values
    def __str__(self):
        return 'The floor is ' + self.identifiers[0] + '. The walls are ' + self.identifiers[1] + '. The ceiling is ' + \
               self.identifiers[2] + '\n' + self.__descr

    def debug(self):
        return self.__descr + "\n" + str(self.getDirections())

    def getTier(self):
        return len(self.getDirections())

    @abc.abstractmethod
    def getEvent(self):
        pass

    def getDirections(self):
        tmp = []
        if self.__north:
            tmp.append('(N)orth')
        if self.__south:
            tmp.append('(S)outh')
        if self.__east:
            tmp.append('(E)ast')
        if self.__west:
            tmp.append('(W)est')
        return tmp

    def getType(self):
        return self.__type

    def getNorth(self):
        return self.__north

    # Implement Me
    def getSouth(self):
        return self.__south

    # Implement Me
    def getEast(self):
        return self.__east

    # Implement Me
    def getWest(self):
        return self.__west

    # Implement Me
    # Mutators
    # Update the values
    def setDescription(self, d):
        self.__descr = d
        return self

    # Implement Me
    def setNorth(self, n, paired=True):
        if paired:
            n.setSouth(self, False)
        self.__north = n
        return self

    # Implement Me
    def setSouth(self, s, paired=True):
        if paired:
            s.setNorth(self, False)
        self.__south = s
        return self

    # Implement Me
    def setEast(self, e, paired=True):
        if paired:
            e.setWest(self, False)
        self.__east = e
        return self

    # Implement Me
    def setWest(self, w, paired=True):
        if paired:
            w.setEast(self, False)
        self.__west = w
        return self
# Implement Me
