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

    if room.right.bats or room.left.bats:
        print("You smell bats...")
    if room.right.wumpus or room.left.wumpus:
        print("You hear a wumpus...")
    if room.right.pit or room.left.pit:
        print("You feel a draft...")

def room_check(room):
    if room.bats:
        #set room to another room
        pass
    if room.pit:
        print("You fell into a bottomless pit...")
        #some lose condition change
    if room.wumpus:
        print("The wumpus ate you....")

def fire_check(room, direction):
    if direction == "right" and room.right.wumpus:
        print("You got the wumpus!")
    if direction == "left" and room.left.wumpus:
        print("You got the wumpus!")
    else:
        print("It seems you have missed...")