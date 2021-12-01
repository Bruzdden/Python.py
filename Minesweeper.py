mina = 1
grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
def click(row, col):
    if grid[row][col] == mina:
        print("konec")
def show_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value = grid[row][col]
            print(f"{value}", end=" ")
        print(" ")
click(0, 2)
show_grid()
