def print_ascii_maze(grid):
    height = len(grid)
    width = len(grid[0])

    for x in range(height):
        # 1. Print North walls (+---+)
        for y in range(width):
            print("+", end="")
            if grid[x][y].walls["N"]:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")
        
        # 2. Print West and East walls (|   |)
        for y in range(width):
            if grid[x][y].walls["W"]:
                print("|", end="")
            else:
                print(" ", end="")
            print("   ", end="") 
        
        # Ekher hayt f l-limen (East dial ekher cell f l-row)
        if grid[x][width-1].walls["E"]:
            print("|")
        else:
            print(" ")
    
    # 3. Print South walls dial ekher row
    for y in range(width):
        print("+", end="")
        if grid[height-1][y].walls["S"]:
            print("---", end="")
        else:
            print("   ", end="")
    print("+")

####################
####################
####################
####################
####################
####################
####################


def print_ascii_maze2(grid):
    """
    grid: 2D list of cell objects with walls dict {"N","E","S","W"}
    """
    height = len(grid)
    width = len(grid[0])

    for x in range(height):
        # print top walls
        for y in range(width):
            print("+", end="")
            if grid[x][y].walls["N"]:
                print("---", end="")
            else:
                print("   ", end="")
        print("+")
        
        # print side walls + cell space
        for y in range(width):
            if grid[x][y].walls["W"]:
                print("|", end="")
            else:
                print(" ", end="")
            print("   ", end="")  # space inside cell
        # last cell East wall
        if grid[x][-1].walls["E"]:
            print("|")
        else:
            print(" ")
    
    # print bottom walls of last row
    for y in range(width):
        print("+", end="")
        if grid[-1][y].walls["S"]:
            print("---", end="")
        else:
            print("   ", end="")
    print("+")
