class Room:
    def __init__(self, bats, wumpus, pit):
        self.bats = bats
        self.wumpus = wumpus
        self.pit = pit
        self.left = None
        self.right = None
        self.below = None

# create pre-defined cave and return entrance room/node
def create_cave():
    node = Room(False, False, False)
    node.right = Room(False, False, False)
    node.left = Room(False, False, False)
    node.right.below = node
    node.left.below = node
    node = node.left
    node.right = Room(False, True, False)
    node.left = Room(True, False, False)
    node = node.below
    node.right.right = Room(False, False, True)
    return node

def print_current_room_info(room):
    if room.right and room.left:
        print("You see two chambers ahead...")
    elif room.right and not room.left or room.left and not room.right:
        print("You see one chamber ahead...")
    else:
        print("Dead end...")

    if room.right:
        if room.right.bats:
            print("You smell bats...")
        if room.right.wumpus:
            print("You hear a wumpus...")
        if room.right.pit:
            print("You feel a draft...")
    if room.left:
        if room.left.bats:
            print("You smell bats...")
        if room.left.wumpus:
            print("You hear a wumpus...")
        if room.left.pit:
            print("You feel a draft...")

def room_check(room):
    if room.bats:
        #set room to another room
        pass
    if room.pit:
        print("You fell into a bottomless pit...")
        return 0
    if room.wumpus:
        print("The wumpus ate you....")
        return 0

def fire_check(room, direction):
    if direction == "right" and room.right.wumpus:
        print("You got the wumpus!")
    if direction == "left" and room.left.wumpus:
        print("You got the wumpus!")
    else:
        print("It seems you have missed...")

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
        print("To move- type 'right' or 'left'\nTo fire, type fire")
        choice = input(">")
        if choice == "right" or choice == "left":
            room = hunter_move_check(room, choice)
            if room_check(room) == 0:
                hunting = False
        if choice == "fire":
            print("Right or Left? ")
            choice = input(">")
            fire_check(room, choice)
        print("\n")

game_loop()