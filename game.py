import random

class Room:
    def __init__(self, bats, wumpus, pit, node_id):
        self.bats = bats
        self.wumpus = wumpus
        self.pit = pit
        self.left = None
        self.right = None
        self.below = None
        self.node_id = node_id

# create pre-defined cave and return entrance room/node
def create_cave():
    node = Room(False, False, False, 1)
    node.right = Room(False, False, False, 2)
    node.left = Room(False, False, False, 3)
    node.right.below = node
    node.left.below = node
    node = node.left
    node.right = Room(False, True, False, 4)
    node.left = Room(True, False, False, 5)
    node.right.below = node
    node.left.below = node
    node = node.below
    node.right.right = Room(False, False, True, 6)
    return node

def print_current_room_info(room):
    if room.right and room.left:
        print("You see two chambers ahead...")
        return 2
    elif room.right and not room.left or room.left and not room.right:
        print("You see one chamber ahead...")
        return 1
    else:
        print("Dead end...")
        return 0

    if room.right: #confirming there is a right room
        if room.right.bats:
            print("You smell bats...")
        if room.right.wumpus:
            print("You hear a wumpus...")
        if room.right.pit:
            print("You feel a draft...")
    if room.left: #confirming there is a left room
        if room.left.bats:
            print("You smell bats...")
        if room.left.wumpus:
            print("You hear a wumpus...")
        if room.left.pit:
            print("You feel a draft...")

def bat_check(room):
    def traverse(random_node, visited, stack):
        while stack:
            current = stack.pop()
            if current in visited or not current:
                continue

            visited.append(current)
            if current.node_id == random_node:
                return current

            stack.append(current.right)
            stack.append(current.left)

    if room.bats:
        root = room.below.below
        stack = []
        visited = []
        stack.append(root)
        return traverse(random.randint(0, 7), visited, stack)
    return room


    if room.bats:
        root = room.below.below
        stack = []
        visited = []
        stack.append(root)
    return room

def room_check(room):
    if room.pit:
        print("You fell into a bottomless pit...")
        return 0
    if room.wumpus:
        print("The wumpus ate you....")
        return 0

def fire_check(room, direction):
    if direction == "right" and room.right.wumpus:
        print("You got the wumpus!")
        return 1
    if direction == "left" and room.left.wumpus:
        print("You got the wumpus!")
        return 1
    else:
        print("It seems you have missed...")
        return 0

def hunter_move_check(room, user_input):
    if user_input == "right":
        if not room.right:
            print("There is no right chamber!")
        else:
            return room.right
    elif user_input == "left":
        if not room.left:
            print("There is no left chamber!")
        else:
            return room.left


def game_loop():
    room = create_cave()
    hunting = True
    while hunting:
        print_current_room_info(room)
        print("To move, type 'right' or 'left'\nTo fire, type fire")
        choice = input(">")
        if choice == "right" or choice == "left":
            room = hunter_move_check(room, choice)
            room = bat_check(room)
            if room_check(room) == 0:
                hunting = False
        if choice == "fire":
            print("Right or Left? ")
            choice = input(">")
            if fire_check(room, choice) == 1:
                hunting = False
        print("\n")

if __name__ == '__main__':
    game_loop()