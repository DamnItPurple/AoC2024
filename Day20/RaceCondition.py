# https://adventofcode.com/2024/day/20
# 

from functools import reduce
import itertools
import time
from collections import defaultdict

INPUT = 'input.txt'

def do_part2(input):
    return do_part1(input, False)

def do_part1(input, do_part_1 = True):
    '''
    1. label path and create list of (coord)
    2. for each key in dict, find out available short cuts 2 picosecs away
    3. tally cheats per distance

    ans = how many cheats to save 100 picosec (0 cheats for input0.txt)
    '''
    def find_next_step(grid, i, j):
        for pos in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            r = pos[0]
            c = pos[1]
            if grid[r][c] == '.' or grid[r][c] == 'E':
                return r, c
        print(f'SHOULD NOT GET HERE')
        return 0,0
    
    def update_cheats(grid, upto):

        def within_bounds(r, c):
            if r < len(grid) and c < len(grid[0]) and r >= 0 and c >= 0:
                return True
            else:
                return False
            
        cheats = defaultdict(int)

        possible = []
        # if upto == 2:
        #     possible = set([(-2,0),(-1,1),(0,2),(1,1),(2,0),(1,-1),(0,-2),(-1,-1)])
        # else:
        for n in range(-upto, upto+1):
            possible.extend([(n,m) for m in range(-upto, upto+1) if (abs(n)+abs(m)<=upto and abs(n)+abs(m)>1)])

        for (i,j) in path_list:
            for pos in possible:
                r = i+pos[0]
                c = j+pos[1]
                if within_bounds(r,c) and isinstance(grid[r][c],int): # found a path
                    savings = grid[r][c] - grid[i][j] - (abs(pos[0])+abs(pos[1]))
                    if savings > 0:
                        cheats[savings] += 1
        return cheats

    ans = 0
    
    path_list = []

    # find S and replace with 0
    for i, row in enumerate(input):
        for j in range(len(row)):
            if row[j] == 'S':
                path_list.append((i,j))
                break
    
    #complete the path
    i = path_list[0][0]
    j = path_list[0][1]
    while True:
        input[i][j] = len(path_list)-1
        i,j = find_next_step(input, i,j)
        path_list.append((i,j))
        if input[i][j] == 'E':
            input[i][j] = len(path_list)-1
            break

    if do_part_1:
        cheats = update_cheats(input, 2)
    else:
        cheats = update_cheats(input, 20)

    # print(f'{cheats}')
    ans = sum([cheats[i] for i in cheats if i >= 100])

    return ans

def process_input(filename):
    '''
    input looks like

    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############

    return input = 2d grid with path (ie each coord is either #, ., S, or E)

    '''

    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    grid = []
    for line in lines:
        grid.append([char for char in line.rstrip()])

    return grid


if __name__ == '__main__':
    '''
    $ python RaceCondition.py 
    start part 1
    do_part1 returns 1411 in 0.05012774467468262 seconds
    start part 2
    do_part2 returns 1010263 in 4.1200573444366455 seconds

    The tough part for me was coming up with expression for where the cheats can land (line 45-46)
    '''
    input = process_input(INPUT)

    # print(input)
    print(f'start part 1')
    start_time = time.time()
    ans = do_part1(input)
    end_time = time.time()
    print(f'do_part1 returns {ans} in {end_time-start_time} seconds')

    input = process_input(INPUT)
    # print(input)
    
    print(f'start part 2')
    start_time = time.time()
    ans = do_part2(input)
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

