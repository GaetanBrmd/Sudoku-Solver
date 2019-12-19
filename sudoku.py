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