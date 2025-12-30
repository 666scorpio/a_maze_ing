import random

class cell:
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

class maze_generator:
    def __init__(self, width, height, entry, exit_):        
        self.count = 0
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit_
        self.grid = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
               cell_object = cell(x, y)
               row.append(cell_object)
            self.grid.append(row)
        self.maze_gen(0, 0)
        self.count = 0
        for x in self.grid:
            for y in x:
                if y.visited:
                    self.count += 1
    
    def the_wall1(self, x, y, x1, y1):
        if x1 > x:
            return "S"
        if x1 < x:
            return "N"
        if y1 > y:
            return "E"
        if y1 < y:
            return "W"    

    def check(self, x, y, neighbors):
        if y + 1 < self.width and not self.grid[x][y + 1].visited:
           neighbors.append((x, y + 1))
        if y - 1 >= 0 and not self.grid[x][y - 1].visited:
           neighbors.append((x, y - 1))
        if x + 1 < self.height and not self.grid[x + 1][y].visited:
           neighbors.append((x + 1, y))
        if x - 1 >= 0 and not self.grid[x - 1][y].visited:
           neighbors.append((x - 1, y))

    def maze_gen(self, x, y):
        self.grid[x][y].visited = True
        neighbors = []
        self.check(x, y, neighbors)
        c = len(neighbors)
        if neighbors:
            i = 0
            while i < c:
                neighbors = []
                self.check(x, y, neighbors)
                c = len(neighbors)
                if (neighbors):
                    chosen = random.choice(neighbors)
                    x1, y1 = chosen
                    wall = self.the_wall1(x, y, x1, y1)
                    opposite = {"N":"S","S":"N","W":"E","E":"W"}
                    self.grid[x][y].walls[wall] = False
                    self.grid[x1][y1].walls[opposite[wall]] = False
                    self.maze_gen(x1, y1)
                i += 1
        else:
            return None



from maze_printer import print_ascii_maze
width = 8
height = 6
maze = maze_generator(width, height, 0, 0)
#maze.print_maze()
print_ascii_maze(maze.grid)
print(maze.count)







