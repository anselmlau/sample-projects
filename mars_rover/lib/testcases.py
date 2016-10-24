import unittest
from main import *


class ReadFileTestCase(unittest.TestCase):

    filename = 'test_input.txt'

    def test_file_exists(self):

        self.assertTrue(os.path.isfile(self.filename), 'Input file does not exist.')

    def test_read_file_content(self):

        tmp_lines = read_file_to_list(self.filename)
        self.assertTrue(len(tmp_lines) > 0, 'No content read.')


class GridInstanceTestCase(unittest.TestCase):

    def setUp(self):
        Grid.instance(size_x=5, size_y=5)

    def test_grid_initialized(self):

        self.assertTrue(Grid.instance().get_size() == (5, 5))

    def test_is_position_inside_valid(self):

        self.assertTrue(Grid.instance().is_position_valid(2, 4))

    def test_is_position_outside_valid(self):

        self.assertFalse(Grid.instance().is_position_valid(7, 4))
        self.assertFalse(Grid.instance().is_position_valid(2, 6))
        self.assertFalse(Grid.instance().is_position_valid(8, 7))

    def test_is_position_on_edge_valid(self):

        self.assertTrue(Grid.instance().is_position_valid(5, 5))
        self.assertTrue(Grid.instance().is_position_valid(0, 5))
        self.assertTrue(Grid.instance().is_position_valid(5, 0))
        self.assertTrue(Grid.instance().is_position_valid(0, 0))

    def test_is_negative_position_valid(self):

        self.assertFalse(Grid.instance().is_position_valid(-2, 2))

    def test_is_null_position_valid(self):

        self.assertFalse(Grid.instance().is_position_valid(None, 2))

    def tearDown(self):
        Grid.instance().drop()


class RoverTestCase(unittest.TestCase):

    def test_rover_init(self):

        rover = Rover(x=1, y=2, head='N', id=1)
        self.assertTrue(rover.get_state() == '1 2 N', 'Incorrect initialization output for rover 1')

        rover = Rover(x=3, y=3, head='E', id=1)
        self.assertTrue(rover.get_state() == '3 3 E', 'Incorrect initialization output for rover 2')


class NavigateTestCase(unittest.TestCase):

    rover1 = Rover()
    rover2 = Rover()

    def setUp(self):

        Grid.instance(size_x=5, size_y=5)

        # only updating variables in such a manner for unittests
        self.rover1.x = 1
        self.rover1.y = 2
        self.rover1.head = 'N'
        self.rover1.id = 1

        self.rover2.x = 3
        self.rover2.y = 3
        self.rover2.head = 'E'
        self.rover2.id = 2

    def test_output_correctness(self):

        self.rover1.navigate(cmds='LMLMLMLMM')
        self.assertTrue(self.rover1.get_state() == '1 3 N', 'Incorrect output for rover 1')
        self.rover2.navigate(cmds='MMRMMRMRRM')
        self.assertTrue(self.rover2.get_state() == '5 1 E', 'Incorrect output for rover 2')

    def test_out_of_bounds(self):

        self.rover1.navigate(cmds='LMLMLMLMMMMMMRM')
        self.assertTrue(self.rover1.get_state() == '2 5 E', 'Incorrect output for rover 1 in out of bounds case')

    def test_bad_commands(self):

        self.rover1.navigate(cmds='#LxMLMLMLM2M')
        self.assertTrue(self.rover1.get_state() == '1 3 N', 'Bad commands not handled correctly')

    def test_lowercase_commands(self):

        self.rover1.navigate(cmds='lmlmLmlmm')
        self.assertTrue(self.rover1.get_state() == '1 3 N', 'Lowercase commands not handled correctly')

    def test_empty_command(self):

        self.rover1.navigate(cmds='')
        self.assertTrue(self.rover1.get_state() == '1 2 N', 'Empty commands not handled correctly')

    def test_turn_right(self):

        self.rover1.navigate(cmds='R')
        self.assertTrue(self.rover1.head == 'E', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='R')
        self.assertTrue(self.rover1.head == 'S', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='R')
        self.assertTrue(self.rover1.head == 'W', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='R')
        self.assertTrue(self.rover1.head == 'N', 'Incorrect heading output for right turn')

    def test_turn_left(self):

        self.rover1.navigate(cmds='L')
        self.assertTrue(self.rover1.head == 'W', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='L')
        self.assertTrue(self.rover1.head == 'S', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='L')
        self.assertTrue(self.rover1.head == 'E', 'Incorrect heading output for right turn')
        self.rover1.navigate(cmds='L')
        self.assertTrue(self.rover1.head == 'N', 'Incorrect heading output for right turn')

    def tearDown(self):

        Grid.instance().drop()
        self.rover1 = None
        self.rover2 = None

if __name__ == '__main__':
    unittest.main()
