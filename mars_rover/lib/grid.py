from logger import Logger


class Grid(object):

    _instance = None
    _size = None

    def __init__(self):
        #
        if self._instance:
            msg = 'Class must be accessed through instance()'
            Logger.log_error(cls=__name__, msg=msg)

        else:
            pass

    @classmethod
    def instance(cls, size_x=None, size_y=None):
        """
        Singleton implementation
        Instantiate Grid if no instance of Grid class
        Return instance
        """

        if cls._instance is None:

            if size_x is None or size_y is None:
                msg = 'x and y dimension of grid must be provided to instantiate'
                Logger.log_error(cls=__name__, msg=msg)

            # if no instance, create new instance and set size
            cls._instance = Grid()
            cls._instance.__set_size(size_x, size_y)

        else:
            # if instance exists, do not modify size
            if size_x is not None or size_y is not None:
                Logger.log_warn(cls=__name__,
                                msg='Grid size is already set and cannot be modified')

        return cls._instance

    def drop(self):
        """
        Remove instance for unittests
        """

        # remove instance for unittests
        self._instance = None

    def __set_size(self, size_x, size_y):
        """
        Set max size x and y of grid
        """

        try:
            # check if size x and y is numeric
            size_x = int(size_x)
            size_y = int(size_y)

        except TypeError, e:
            msg = 'grid size input cannot be cast as int - x: {}, y: {}'.format(size_x, size_y)
            Logger.log_error(cls=__name__, msg=msg)
            raise

        if size_x < 0:
            Logger.log_error(cls=__name__, msg='size x set as non-positive integer')

        if size_y < 0:
            Logger.log_error(cls=__name__, msg='size y set as non-positive integer')

        self._size = (size_x, size_y)  # store as tuple

    def get_size(self):
        """
        Return max size of x, max size of y
        """

        if not self._size:
            Logger.log_error(cls=__name__, msg='Grid size not set.')

        return self._size[0], self._size[1]

    def is_position_valid(self, x, y):
        """
        Return boolean value indicating if x and y lies within grid
        """

        size_x, size_y = self.get_size()

        # check if x and y-coordinate is within grid
        if x < 0 or y < 0 or x > size_x or y > size_y:
            return False

        return True
