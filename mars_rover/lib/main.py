import sys
import os
from grid import Grid
from rover import Rover
from logger import Logger


def read_file_to_list(filename):
    """
    Return lines of input file as list
    """

    # read input file to list
    if os.stat(filename).st_size == 0:
        Logger.log_warn(cls=__name__, msg='empty input file {} '.format(filename))
        sys.exit()

    # store file contents to list
    f_in = open(filename, 'r')
    content_by_lines = f_in.readlines()
    content_by_lines = [line.strip('\n') for line in content_by_lines]
    f_in.close()

    return content_by_lines


def initialize_grid(specs):
    """
    Initialize grid given specs of x and y max sizes
    """

    # store grid size in tuple
    grid_size = tuple([int(val) for val in specs.split()])

    try:
        # grid size tuple must have only two variables representing max size of x and y
        assert len(grid_size) == 2

    except AssertionError:
        Logger.log_error(cls=__name__,
                         msg='Incorrect number of arguments used to specify grid dimensions')
        raise

    Grid.instance(size_x=grid_size[0], size_y=grid_size[1])


if __name__ == '__main__':

    # store each line to list
    lines = read_file_to_list('test_input.txt')

    initialize_grid(lines[0])  # setup grid
    del lines[0]  # remove first line of input

    if len(lines) == 0:
        Logger.log_info(cls=__name__, msg='Application ended - no rover info')
        sys.exit()

    f_out = open("test_output.txt", "wb")

    for i in xrange(0, len(lines), 2):  # increment i by 2 each iteration

        try:
            initial_state = lines[i]
            commands = lines[i+1]

        except IndexError:
            Logger.log_error(cls=__name__,
                             msg='Index error in getting initial state and commands')
            break

        if not initial_state:  # skip if line is empty
            continue

        rover_id = i // 2 + 1

        try:
            # initial state must return only three variables
            x, y, head = initial_state.split()

        except ValueError:
            Logger.log_warn(cls=__name__,
                            msg='Incorrect number of parameters used to '
                                'specify initial state: Rover {}, State {}'.format(rover_id, str(initial_state)))
            continue

        rover = Rover(x=x, y=y, head=head, id=rover_id)  # instantiate rover

        if None not in (rover.x, rover.y, rover.head):
            rover.navigate(cmds=commands)  # navigate given commands
        else:
            Logger.log_warn(cls=__name__, msg='Bad Initial state input for Rover {}: x={}, y={}, z={}. '
                                              'Navigation not proceeded.'.
                            format(rover.id, rover.x, rover.y, rover.head))
            continue

        # output final position in two formats: console and test_output.txt
        rover.print_state()
        f_out.write('{}\n'.format(rover.get_state()))

    f_out.close()









