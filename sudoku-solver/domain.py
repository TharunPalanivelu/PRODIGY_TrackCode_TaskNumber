import pyautogui as pg
import time

grid = []
while True:
    row = list(input("row :"))
    ints = []
    for n in row:
        ints.append(int(n))
    grid.append(ints)
    if len(grid) == 9:
        break
    print("Row" + str(len(grid)) + "complete")

time.sleep(3)


def possible(x, y, n):
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def print_grid(matrix):
    str_fin = []

    for lists in matrix:
        for num in lists:
            str_fin.append(str(num))
    counter = 0
    for num in str_fin:
        pg.press(num)
        pg.hotkey("right")
        counter += 1
        if counter % 9 == 0:

            pg.hotkey("down")
            for i in range(8):
                pg.hotkey("left")


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_grid(grid)


solve()
