def convert_to_hex(grid, output_file):
    output = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[0])):
            value = 0
            if grid[r][c].walls["N"]:
                value += 1
            if grid[r][c].walls["E"]:
                value += 2
            if grid[r][c].walls["S"]:
                value += 4
            if grid[r][c].walls["W"]:
                value += 8
            row.append(f"{value:X}")
        output.append(''.join(row))
    try:
        with open(output_file, "w") as file:
            for line in output:
                file.write(line + "\n")
    except Exception as error:
        print(error)