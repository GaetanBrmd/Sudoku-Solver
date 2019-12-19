def check(grid, nb, x, y):
    res = True
    #Check the column
    for i in range(9):
        #print(grid[i][y])
        res = res and grid[i][y] != nb
    #print("------")
    #Check the row
    for j in range(9):
        #print(grid[x][j],end=" ")
        res = res and grid[x][j] != nb
    #Check the 3*3 square
    for i in range(3):
        for j in range (3):
            #print(grid[(x//3)*3+i][(y//3)*3+j])
            res = res and grid[(x//3)*3+i][(y//3)*3+j] != nb
    return res


def print_sudoku_grid(grid):
    i=0
    for row in grid :
        if i%3==0 :
                print("+-----------+-----------+-----------+")
        print(("| {}   {}   {} | {}   {}   {} | {}   {}   {} |").format(*[x if x != 0 else " " for x in row]))
        i+=1
    print("+-----------+-----------+-----------+")

if __name__ == "__main__":
    print("Let's start to solve this sudoku !")
    print("Here is the grid :")
    grid = [
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 9, 8],
        [3, 0, 0, 0, 8, 2, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 7, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 7],
        [6, 4, 0, 3, 0, 0, 0, 0, 0],
    ]
    print_sudoku_grid(grid)
    print("Let's check if we can put a number somewhere : ")
    print(check(grid,3,1,1))