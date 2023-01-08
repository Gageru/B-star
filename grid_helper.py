import math
import numpy as np

START_COL = "S"
END_COL = "E"
VISITED_COL = "x"
OBSTACLE_COL = "#"
PATH_COL = "@"


def generate_grid_empty():
    return [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

def generate_grid_obstacle():
    return [[1,   1,   1,   1,   1,   1,   1,   1,   1],
            [1,   1, '#', '#', '#', '#',   1,   1,   1],
            [1,   1,   2,   3,   4, '#',   1,   1,   1],
            [1,   1, '#', '#',   5, '#',   1,   1,   1],
            [1,   1,   1, '#',   6, '#',   1,   1,   1],
            [1,   1,   1, '#',   7, '#',   1,   1,   1],
            [1,   1, '#', '#',   8, '#', '#', '#', '#'],
            [1,   1,   1,   1,   9,  10,  10,  10, '#'],
            [1,   1, '#', '#', '#', '#', '#', '#', '#']]


def generate_grid_weighted():
    return [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#",  1,   1,   1,   1,   1,   1, "#",   6, "#",   1,   1,   1, "#",   8,  "#"],
            ["#",  1,   1,   1,   1,   1,   1, "#",   5, "#",   1,   1,   1,   6,   7,  "#"],
            ["#",  1, "#", "#",   1, "#", "#", "#",   4, "#", "#", "#", "#",   5, "#",  "#"],
            ["#",  1,   1,   2,   3,   2,   1,   2,   3,   1,   1,   1,   1,   4,   1,  "#"],
            ["#",  1, "#", "#",   4, "#", "#", "#",   4,   3,   2,   1,   1,   3, "#",  "#"],
            ["#",  1,   1, "#",   5, "#",   9, "#",   5, "#", "#",   2,   1,   2, "#",  "#"],
            ["#",  1,   1, "#",   6,   7,   8, "#",   6, "#",   4,   3, "#",   1,   1,  "#"],
            ["#",  2, "#", "#",   7, "#", "#", "#",   7, "#",   5,   4, "#",   1,   1,  "#"],
            ["#",  3,   4,   5,   6,   1,   1,   1,   8,   7,   6, "#", "#",   1, "#",  "#"],
            ["#",  1, "#", "#",   5, "#", "#", "#",   8, "#",   7,   8,   1,   1, "#",  "#"],
            ["#",  1,   1, "#",   4, "#",   8,   9,  10,   1,   1,   9,  10,   1,   1,  "#"],
            ["#",  1,   1, "#",   3, "#",   7,   1,   1,   1, "#",   1, "#", "#",   1,  "#"],
            ["#",  1,   1,   1,   2,   1,   6, "#",   1, "#",   1,   1, "#",   1,   1,  "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]


def heuristic_distance(pos, end_pos, type="e"):
    """
    m - manhattan
    e - euclidean
    """

    dx = abs(pos[0] - end_pos[0])
    dy = abs(pos[1] - end_pos[1])

    if type == "m":
        return dx + dy

    return math.sqrt(dx * dx + dy * dy)


def find_path(start, end, came_from):
    path = [end]

    current = end
    while current != start:
        current = came_from[current]
        path.append(current)

    # reverse to have Start -> Target
    # just looks nicer
    path.reverse()
    return path


def get_cost(grid, pos):
    col_val = grid[pos[0]][pos[1]]
    return int(col_val) if type(col_val) is int else 1


def get_neighbors(grid, row, col):
    height = len(grid)
    width = len(grid[0])

    neighbors = [(row + 1, col), (row, col - 1), (row - 1, col), (row, col + 1)]

    if (row + col) % 2 == 0:
        neighbors.reverse()

    # поиск кандидатов
    neighbors = filter(lambda t: (0 <= t[0] < height and 0 <= t[1] < width), neighbors)
    # исключение из кандитатов препятсвий
    neighbors = filter(lambda t: (grid[t[0]][t[1]] != OBSTACLE_COL), neighbors)

    return neighbors

def cvt_format_map(grid):
    grid = np.where(grid == OBSTACLE_COL, -3, grid)
    grid = np.where(grid == START_COL, -2, grid)
    grid = np.where(grid == END_COL, -1, grid)
    grid = np.where(grid == PATH_COL, 0, grid)
    return grid.astype(np.int)

def draw_sf(path, grid):
    # отрисовка старта и финиша
    start_pos = path[0]
    end_pos = path[-1]
    grid[start_pos[0]][start_pos[1]] = START_COL
    grid[end_pos[0]][end_pos[1]] = END_COL

    return grid
