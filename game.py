class Room:
    def __init__(self, bats, wumpus, pit):
        self.bats = bats
        self.wumpus = wumpus
        self.pit = pit
        self.left = None
        self.right = None