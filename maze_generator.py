import random
from hexa_writer import convert_to_hex

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"N": True, "E": True, "W": True, "S": True}
        self.visited = False
    def print_walls(self):
        for wall in self.walls.values():
            if wall:
                print("1", end="")
            else:
                print("0", end="")

class MazeGenerator:
    def __init__(self, width, height, entry, exit_, seed, perfect):        
        self.count = 0
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit_
        self.grid = []
        self.seed = seed
        self.perfect = perfect
        for x in range(self.height):
            row = []
            for y in range(self.width):
               cell_object = Cell(x, y)
               row.append(cell_object)
            self.grid.append(row)
        if seed is not None:
            random.seed(seed)
        self.maze_gen(0, 0)
        convert_to_hex(self.grid, "maze.txt")
        self.count = 0
        for x in self.grid:
            for y in x:
                if y.visited:
                    self.count += 1

    def the_wall(self, x, y, x1, y1):
        if x1 > x:
            return "S"
        if x1 < x:
            return "N"
        if y1 > y:
            return "E"
        if y1 < y:
            return "W"    

    def neighbors_check(self, x, y, neighbors):
        if y + 1 < self.width and not self.grid[x][y + 1].visited:
           neighbors.append((x, y + 1))
        if y - 1 >= 0 and not self.grid[x][y - 1].visited:
           neighbors.append((x, y - 1))
        if x + 1 < self.height and not self.grid[x + 1][y].visited:
           neighbors.append((x + 1, y))
        if x - 1 >= 0 and not self.grid[x - 1][y].visited:
           neighbors.append((x - 1, y))

    def maze_gen(self, x, y):
        if self.grid[x][y].visited:
            return None
        self.grid[x][y].visited = True
        neighbors = []
        self.neighbors_check(x, y, neighbors)
        neighbors_count = len(neighbors)
        i = 0
        while i < neighbors_count:
            neighbors = []
            self.neighbors_check(x, y, neighbors)
            neighbors_count = len(neighbors)
            if (neighbors):
                chosen = random.choice(neighbors)
                x1, y1 = chosen
                wall = self.the_wall(x, y, x1, y1)
                opposite = {"N":"S","S":"N","W":"E","E":"W"}
                self.grid[x][y].walls[wall] = False
                self.grid[x1][y1].walls[opposite[wall]] = False
                self.maze_gen(x1, y1)
            i += 1

        def place_42_pattern(grid):
            if self.height < 8 or self.width < 11:
                raise ValueError("the fucking maze too small for the fucking pattern")
            pattern_4 = [
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
            ]
            pattern_2 = [
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ]
            pattern_height = 8
            pattern_width = 10
            center_row = (self.height - pattern_height) // 2
            center_col = (self.width - pattern_width) // 2
            starts = []
            for start_row in range(1, self.height - pattern_height):
                for start_col in range(1, self.width - pattern_width):
                    starts.append()

from maze_printer import print_ascii_maze
width = int(input("width "))
height = int(input("height "))
maze = MazeGenerator(width, height, 0, 0, 42, False)
#maze.print_maze()
print_ascii_maze(maze.grid)
#print(maze.count)
