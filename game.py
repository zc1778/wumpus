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
