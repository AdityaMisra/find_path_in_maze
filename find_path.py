def is_cell_in_constraints(maze, x, y, n, m):
    if n > x >= 0 and m > y >= 0 and maze[x][y] == 1:
        return True
    return False


def find_path(maze, x, y, cells_travelled,  n, m):

    if x == n - 1 and y == m - 1:
        cells_travelled.append((x, y))
        return True

    if is_cell_in_constraints(maze, x, y, n, m):

        if not (x, y) in cells_travelled:
            cells_travelled.append((x, y))
        else:
            return False

        if find_path(maze, x + 1, y, cells_travelled, n, m):
            return True

        if find_path(maze, x, y + 1, cells_travelled, n, m):
            return True

        if find_path(maze, x - 1, y, cells_travelled, n, m):
            return True

        if find_path(maze, x, y - 1, cells_travelled, n, m):
            return True

        cells_travelled.remove((x, y))
        return False


def find_path_in_maze(maze, n, m):
    cells_travelled = []

    if not find_path(maze, 0, 0, cells_travelled, n, m):
        print("No path found!")
        return False

    for each_cell in cells_travelled:
        print(each_cell)


if __name__ == "__main__":
    _maze = [[1, 1, 0, 0, 0],
             [0, 1, 1, 1, 1],
             [0, 1, 1, 0, 1],
             [0, 0, 0, 0, 1]]
    _n = 4
    _m = 5
    find_path_in_maze(_maze, _n, _m)
