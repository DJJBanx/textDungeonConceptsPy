from objects import Room, Rooms
from objects.Maze import Maze
from objects.Rooms import *
from util.colors import Colors
import random

cols = Colors()


def disable():
    cols.disable(__name__)


N = 13

rooms = []

for i in range(0, N):
    r = random.randint(1, 100)
    room = None
    if r < 30:
        room = EmptyRoom()
    elif r < 60:
        room = FightRoom()
    elif r < 80:
        room = ChestRoom()
    else:
        room = TrapRoom()
    rooms.append(room)

start = EmptyRoom(-1)
end = EmptyRoom(1)
rooms.append(start)
rooms.append(end)

t1 = []
t2 = []
t3 = []
t4 = []

tiers = [rooms, t1, t2, t3, t4]

#  + random.randint(0,N//4)

i = 0
if N == 1:
    N = 3
while i < (N + N // 3.5):
    print(tiers)
    if len(tiers[0]) < 1 and len(tiers[1]) < 2:
        print('Dungeon exploded!')
        break;
    first = None
    second = None
    if len(tiers[0]) > 0:
        first = tiers[0][random.randint(0, len(tiers[0]) - 1) if len(tiers[0]) > 1 else 0]
        tiers[0].remove(first)
    else:
        total = 50
        if len(tiers[2]) > 0:
            total += 30
            if len(tiers[3]) > 0:
                total += 20
        chance = random.randint(1, total)
        if chance <= 50:
            first = tiers[1][random.randint(0, len(tiers[1]) - 1) if len(tiers[1]) > 1 else 0]
            tiers[1].remove(first)
        elif chance <= 80:
            first = tiers[2][random.randint(0, len(tiers[2]) - 1) if len(tiers[2]) > 1 else 0]
            tiers[2].remove(first)
        else:
            first = tiers[3][random.randint(0, len(tiers[3]) - 1) if len(tiers[3]) > 1 else 0]
            tiers[3].remove(first)
    if len(tiers[0]) > 0:
        second = tiers[0][random.randint(0, len(tiers[0]) - 1) if len(tiers[0]) > 1 else 0]
        tiers[0].remove(second)
    else:
        total = 50
        if len(tiers[2]) > 0:
            total += 30
            if len(tiers[3]) > 0:
                total += 20
        chance = random.randint(1, total)
        if chance <= 50:
            second = tiers[1][random.randint(0, len(tiers[1]) - 1) if len(tiers[1]) > 1 else 0]
            tiers[1].remove(second)
        elif chance <= 80:
            second = tiers[2][random.randint(0, len(tiers[2]) - 1) if len(tiers[2]) > 1 else 0]
            tiers[2].remove(second)
        else:
            second = tiers[3][random.randint(0, len(tiers[3]) - 1) if len(tiers[3]) > 1 else 0]
            tiers[3].remove(second)
    chance = random.randint(1, 4)
    fdirections = first.getDirections()
    sdirections = second.getDirections()
    if chance == 1 and not ('(N)orth' in fdirections) and not ('(S)outh' in sdirections):
        first.setNorth(second)
    elif chance == 2 and not ('(W)est' in fdirections) and not ('(E)ast' in sdirections):
        first.setWest(second)
    elif chance == 3 and not ('(S)outh' in fdirections) and not ('(N)orth' in sdirections):
        first.setSouth(second)
    elif chance == 4 and not ('(E)ast' in fdirections) and not ('(W)est' in sdirections):
        first.setEast(second)
    else:
        print('Worlds collided!')
        i -= 1

    tiers[first.getTier()].append(first)
    tiers[second.getTier()].append(second)
    i += 1

print(tiers)
"""
rooms.append(EmptyRoom(-1))
rooms.append(EmptyRoom())
rooms.append(TrapRoom())
rooms.append(FightRoom())
rooms.append(ChestRoom())
rooms.append(EmptyRoom(1))

rooms[0].setNorth(rooms[1])
rooms[0].setWest(rooms[2])
rooms[1].setEast(rooms[3])
rooms[3].setEast(rooms[5])
rooms[3].setNorth(rooms[4])
"""

my_maze = Maze(start, end)

playing = True

print(cols.LIGHT_YELLOW)

while playing:
    location = my_maze.getCurrent()
    directions = location.getDirections()
    print(location)
    # print(location.debug())
    options = cols.MAGENTA
    if len(directions) > 0:
        for i, value in enumerate(directions):
            options = options + value + ', '
            directions[i] = value.lower()[1]
    inp = input('Enter direction to move: ' + options + '(R)estart.\n' + cols.LIGHT_YELLOW)
    if len(inp) < 1:
        inp = 'failed'
    if inp.lower()[0] == 'n' and inp.lower()[0] in directions:
        print('You went North!')
        my_maze.moveNorth()
    elif inp.lower()[0] == 'w' and inp.lower()[0] in directions:
        print('You went West!')
        my_maze.moveWest()
    elif inp.lower()[0] == 'e' and inp.lower()[0] in directions:
        print('You went East!')
        my_maze.moveEast()
    elif inp.lower()[0] == 's' and inp.lower()[0] in directions:
        print('You went South!')
        my_maze.moveSouth()
    elif inp.lower() == 'reset':
        my_maze.reset()
    else:
        print("Direction invalid, try again.")
        continue

    if my_maze.atExit():
        print(cols.CYAN + "You found the Exit!" + cols.LIGHT_YELLOW)
        exiting = True
        while exiting:
            answer = input('Would you like to exit: ' + cols.MAGENTA + '(Y)es, (N)o.\n' + cols.LIGHT_YELLOW)
            if answer.lower()[0] == 'y':
                playing = False
                exiting = False
            elif answer.lower()[0] == 'n':
                exiting = False
            else:
                print('Input invalid, try again.')
