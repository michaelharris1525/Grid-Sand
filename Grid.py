from copy import deepcopy
class Grid:
    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, hieght, and array. Initially all locations hold None.
        """
        self.array = [[None for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        
    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if not self.in_bounds(x, y):
            raise IndexError(
                f"out of bounds get({x}, {y}) on grid width {self.width}, height {self.height}")

        return self.array[y][x]

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(3,3)
        >>> grid.set(2, 1, "Milk")
        >>> grid.set(0, 2, "Dud")
        >>> grid.get(2, 1)
        Milk
        """
        if not self.in_bounds(x, y):
            raise IndexError(
                f"out of bounds set({x}, {y}, {val}) on grid width {self.width}, height {self.height}")

        self.array[y][x] = val

    def in_bounds(self, x, y):
        """Returns True if the (x, y) is in bounds of the grid. False otherwise."""
        return (x >= 0 and x < self.width) and (y >= 0 and y < self.height)

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        # Grid.build(self.array)
        return f"Grid.build({repr(self.array)})"
        # return f"Grid(height={len(self.height)}, width={len(self.width)} data={self.array}"
        # return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list) :
            return self.array == other
        else:
            return False

    @staticmethod 
    def check_list_malformed(grid) :
        
        # checks to see if the grid/list is a list and is checking if grid is empty or not
        if not isinstance(grid, list) or len(grid) == 0 :
            raise ValueError("You screwed up on the value of your list or grid because its not a list")

        for row in grid:
            if not isinstance(row, list):
                # checks to see if each element is an object of a list and has the same length on each rows
                raise ValueError("Each element of the grid must be a list. You don't have it as the same type")
            if len(row) != len(grid[0]):
                raise ValueError("Each row of the grid is not of the same length :()")
        
        
    @staticmethod
    def build(grid) :
        Grid.check_list_malformed(grid)

        row_length = len(grid[0])
        row_height = len(grid)
        new_grid = Grid((row_length), (row_height))
        new_grid.array = deepcopy(grid)
        return new_grid
    
    def copy(self) :
        return Grid.build(self.array)