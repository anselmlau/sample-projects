from grid import Grid
from logger import Logger


class Rover(object):

    _move_map = {
        'N': 1,
        'E': 1,
        'S': -1,
        'W': -1
    }

    _turn_right_map = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    _turn_left_map = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    def __init__(self, x=None, y=None, head=None, id=None):

        self.id = id
        self.x = x
        self.y = y
        self.head = head

    @property
    def x(self):
        """
        Return x-coordinate as int
        """

        if self.__x is None:
            return None
        else:
            return int(self.__x)

    @x.setter
    def x(self, value):
        """
        Update x-coordinate
        """

        try:
            assert int(value) >= 0
            self.__x = int(value)

        except (TypeError, AssertionError):
            Logger.log_error(cls=__name__,
                             msg='Rover {} - rover x-coordinate must be a zero or positive number'
                             .format(self.id))

            self.__x = None

    @property
    def y(self):
        """
        Return y-coordinate as int
        """

        if self.__y is None:
            return None
        else:
            return int(self.__y)

    @y.setter
    def y(self, value):
        """
        Update y-coordinate
        """

        try:
            assert int(value) >= 0
            self.__y = int(value)

        except (TypeError, AssertionError):
            Logger.log_error(cls=__name__,
                             msg='Rover {} - rover y-coordinate must be a zero or positive number'
                             .format(self.id))

            self.__y = None

    @property
    def head(self):
        """
        Return head as string
        """

        return self.__head

    @head.setter
    def head(self, new_head):
        """
        Update new head
        """

        self.__head = str(new_head)

    @property
    def id(self):
        """
        Return rover id as int
        """

        return self.__id

    @id.setter
    def id(self, value):
        """
        Set rover id
        """

        try:
            self.__id = value

        except TypeError:
            Logger.log_error(cls=__name__,
                             msg='Rover {} - id must be numeric'.format(self.id))
            raise

    def move(self):
        """
        Update x and y-coordinate based on current heading
        """

        x = self.x
        y = self.y

        if self.head in ('N', 'S'):
            y += int(Rover._move_map[self.head])

        elif self.head in ('E', 'W'):
            x += int(Rover._move_map[self.head])

        else:
            return

        # check if new position is valid - update position if valid
        if Grid.instance().is_position_valid(x, y):
            self.x = x
            self.y = y
        else:
            Logger.log_warn(cls=__name__,
                            msg='Position not updated: x={}, y={} is outside of grid area. '
                            .format(x, y))

    def turn_right(self):
        """
        Update head to turn right
        """

        self.head = Rover._turn_right_map[self.head]

    def turn_left(self):
        """
        Update head to turn left
        """

        self.head = Rover._turn_left_map[self.head]

    def navigate(self, cmds=None):
        """
        Update x and y-coordinate based on list of commands
        """

        if not cmds:
            Logger.log_warn(cls=__name__,
                            msg='Rover {} - No command for navigation'.format(self.id))

            return

        for cmd in cmds:

            # process each cmd
            if cmd in ('R', 'r'):
                self.turn_right()

            elif cmd in ('L', 'l'):
                self.turn_left()

            elif cmd in ('M', 'm'):
                self.move()

            else:
                Logger.log_warn(cls=__name__,
                                msg='Rover {} - Unrecognizable command {}'.format(self.id, cmd))

                continue  # if command not recognized, move to next command

    def print_state(self):
        """
        Print current state to console - x and y-coordinate and heading
        """

        print '{} {} {}'.format(self.x, self.y, self.head)

    def get_state(self):
        """
        Return current state - x and y-coordinate and heading
        """

        return '{} {} {}'.format(self.x, self.y, self.head)


