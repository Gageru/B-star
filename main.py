
import argparse
import numpy as np
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
from queue import PriorityQueue

import grid_helper as gh
from pprint import pprint

def find_path_b_star(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}

    while not pq.empty():
        current_pos = pq.get()[1]

        if current_pos == end:
            break

        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            if neighbor not in came_from:
                priority = gh.heuristic_distance(neighbor, end, type="m")
                pq.put((priority, neighbor))
                came_from[neighbor] = current_pos
    return came_from

def find_path_a_star(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    costs = {start: 0}
    while not pq.empty():
        current_pos = pq.get()[1]

        if current_pos == end:
            break

        neighbors = gh.get_neighbors(grid, current_pos[0], current_pos[1])
        for neighbor in neighbors:
            new_cost = costs[current_pos] + gh.get_cost(grid, neighbor)

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority = new_cost + gh.heuristic_distance(neighbor, end, type='e')
                pq.put((priority, neighbor))
                came_from[neighbor] = current_pos

    return came_from

def draw(initial_grid, close_goal, start, end):
    # визуализация карты
    initial_grid = gh.cvt_format_map(initial_grid)
    if not close_goal.tolist(): 
        close_goal = np.array([end])

    clrs = [[0, 0.0, 0.0], [0, 0.0, 1.0], 
            [0, 0.6, 0.0], [1, 1.0, 1.0], 
            [1, 0.9, 0.9], [1, 0.8, 0.8], 
            [1, 0.7, 0.7], [1, 0.6, 0.6], 
            [1, 0.5, 0.5], [1, 0.4, 0.4], 
            [1, 0.3, 0.3], [1, 0.2, 0.2], 
            [1, 0.1, 0.1], [1, 0.0, 0.0]]

    cmap = colors.ListedColormap(np.array(clrs))
    bounds = range(-3, 10, 1)
    norm = colors.BoundaryNorm(bounds, cmap.N)

    _, ax = plt.subplots()
    ax.imshow(initial_grid, cmap=cmap, norm=norm)
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    ax.set_xticks(np.arange(-.5, len(initial_grid[0]), 1))
    ax.set_yticks(np.arange(-.5, len(initial_grid[:,0]), 1))
    plt.plot(close_goal[:, 1], close_goal[:, 0], '-g', linewidth=3)
    plt.show()
    
SEARCH_FUNC = {'a*' : find_path_a_star,
               'b*' : find_path_b_star}

GENERATE_GRID_FUNC = {'empty' : gh.generate_grid_empty,
                      'obstacle' : gh.generate_grid_obstacle,
                      'big' : gh.generate_grid_weighted}

parser = argparse.ArgumentParser()
parser.add_argument('--algorithm', choices=SEARCH_FUNC.keys(), default=find_path_b_star)
parser.add_argument('--grid', choices=GENERATE_GRID_FUNC.keys(), default=gh.generate_grid_empty)
parser.add_argument('--start', nargs='+', type=int, default=[1, 1])
parser.add_argument('--finish', nargs='+', type=int, default=[7, 7])

if __name__ == "__main__":
    args = parser.parse_args()
    
    start, end = tuple(args.start), tuple(args.finish)
    initial_grid = GENERATE_GRID_FUNC[args.grid]()

    came_from = SEARCH_FUNC[args.algorithm](initial_grid, start, end)
    path = gh.find_path(start, end, came_from)
    gh.draw_sf(path, initial_grid)

    draw(np.array(initial_grid), np.array(path), start, end)
