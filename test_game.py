import unittest
from game import hunter_move_check, create_cave, print_current_room_info, fire_check

class TestGameFunctions(unittest.TestCase):

    def test_left_room_movement(self):
        entrance = create_cave()
        checked_room = entrance.left
        self.assertEqual(hunter_move_check(entrance, "left"), checked_room)

    def test_right_room_movement(self):
        entrance = create_cave()
        checked_room = entrance.right
        self.assertEqual(hunter_move_check(entrance, "right"), checked_room)

    def test_room_chamber_info(self):
        entrance = create_cave()
        self.assertEqual(print_current_room_info(entrance), 2)
        entrance = entrance.right
        self.assertEqual(print_current_room_info(entrance), 1)

    def test_fire_check(self):
        entrance = create_cave()
        self.assertEqual(fire_check(entrance, "right"), 0)
        entrance = entrance.left
        self.assertEqual(fire_check(entrance, "right"), 1)


if __name__ == '__main__':
    unittest.main()