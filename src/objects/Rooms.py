from src.objects.Room import Room
import random;

trap_rooms_descr = [
    "You enter a room with an incredibly low ceiling. About 3 feet. As you crawl your way through you find a hatch in the middle.",
    "You hear gears spinning. Ropes pulling. You should be very careful. Something doesn't feel right.",
    "You enter the room. *Click*. Ohhhh shit.",
    "A dark presence seems to be in this room. You better be on your guard!"
]
empty_rooms_descr = [
    "Moist... Wet... Dank...",
    "There is a table in the middle of the room. Otherwise it's empty.",
    "The room is completely empty. Except for the severed hand in the corner. But who cares... Right?",
    "Wow... its hot in here.",
    "...",
    "Banners! So many banners! But there appears to be nothing else... but banners."
]
fight_rooms_descr = [
    "A dark presence seems to be in this room. You better be on your guard!",
    "You hear wild screeching. It is loud. It is coming.",
    "You enter the room and it seems normal. Then everything goes dark. This is not good.",
    "Your hair stands up on the back of your neck as you enter the room. Something is about to happen.",
    "You enter a room that is oddly familiar. Is this your bedroom? From back home? There is a chest lying in the middle of the room... You remember that mimics lie within these walls...",
]
"""
fight_scenarios = [
    ('Ogre', 3),
    ('Knight', 4),
    ('Troll', 2),
    ('Toadstool', 1)
]"""
chest_rooms_descr = [
    "The room is moist... and dank... You found a chest!",
    "You search the room, scouring, scratching for something new... Then you see it... A small jewelry box...",
    "You enter a large stone chamber. A large wooden box lies at the center.. Ooooo... Ominous...",
    "You found a room that is similar to a school. It has tables and chairs... and a chest!",
    "You enter a room with an incredibly low ceiling. About 3 feet. As you crawl your way through you find a hatch in the middle.",
    "As you enter the room, you feel a holy presence. Organ music starts playing, choirs can be heard. The heavens open up! Jesus comes downs the stairs of heaven to bring you a chest!",
    "Beep Beep Beep. Boop Boop Boop. A robot sits in the middle of the room... holding a chest!",
    "You enter a room that is oddly familiar. Is this your bedroom? From back home? There is a chest lying in the middle of the room... You remember that chest mimics lie within these walls..."
]


class TrapRoom(Room):
    def __init__(self):
        super().__init__(trap_rooms_descr[random.randint(0,len(trap_rooms_descr)-1)])

    def getEvent(self):
        pass


class FightRoom(Room):
    def __init__(self):
        super().__init__(fight_rooms_descr[random.randint(0, len(fight_rooms_descr)-1)])

    def getEvent(self):
        pass


class ChestRoom(Room):
    def __init__(self):
        super().__init__(chest_rooms_descr[random.randint(0, len(chest_rooms_descr)-1)])

    def getEvent(self):
        pass


class EmptyRoom(Room):
    def __init__(self, type=0):
        super().__init__(empty_rooms_descr[random.randint(0, len(empty_rooms_descr)-1)], type)

    def getEvent(self):
        pass
