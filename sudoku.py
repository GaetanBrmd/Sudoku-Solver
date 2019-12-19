def check(grid, nb, x, y):
    res = True
    # print("I check the value", nb, "at", x, y)
    '''
    if x==1 and y==0 and nb==8:
        print("Bonne solution")
    if x==2 and y==0 and nb==6:
        print("bonne sol2")
    if x == 3 and y == 0 and nb == 9:
        print("bonne sol3")
        '''
    # Check the column
    for i in range(9):
        # print(grid[i][x])
        res = res and grid[i][x] != nb
    # print("------")
    # Check the row
    for j in range(9):
        # print(grid[y][j],end=" ")
        res = res and grid[y][j] != nb
    # Check the 3*3 square
    # print("\n------")
    for i in range(3):
        for j in range(3):
            # print(grid[(x//3)*3+i][(y//3)*3+j])
            res = res and grid[(x // 3) * 3 + i][(y // 3) * 3 + j] != nb
    # print(res)
    return res

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_sudoku_grid(grid):
    i = 0
    for row in grid:
        if i % 3 == 0:
            print("+-----------+-----------+-----------+")
        print("| {}   {}   {} | {}   {}   {} | {}   {}   {} |".format(*[x if x != 0 else " " for x in row]))
        i += 1
    print("+-----------+-----------+-----------+")

def find_next(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

def solve(grid):
    find = find_next(grid)
    if not find:
        return True
    else:
        row, col = find
    nb=1
    while nb<10:
        if valid(grid, nb, (row, col)):
            grid[row][col] = nb
            if solve(grid):
                return True
            grid[row][col] = 0
        nb+=1

    return False


if __name__ == "__main__":
    print("Let's start to solve this sudoku !")
    print("Here is the grid :")
    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    '''grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]'''
    print_sudoku_grid(grid)
    # print("Let's check if we can put a number somewhere : ")
    # print(check(grid, 1, 1, 0))
    solve(grid)
    print_sudoku_grid(grid)
