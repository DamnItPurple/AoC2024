# https://adventofcode.com/2024/day/10
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
    return sum of product

    '''
    def hike(val,padded,i,j):
        # look for val in adjuacent cells
        ret = []
        if val == 9:
            if padded[i][j-1] == 9:
                # print(f'trailhead at {i},{j-1}')
                ret.append((i,j-1))
            if padded[i][j+1] == 9:
                # print(f'trailhead at {i},{j+1}')
                ret.append((i,j+1))
            if padded[i-1][j] == 9:
                # print(f'trailhead at {i-1},{j}')
                ret.append((i-1,j))
            if padded[i+1][j] == 9:
                # print(f'trailhead at {i+1},{j}')
                ret.append((i+1,j))
        else:
            if padded[i][j-1] == val:
                ret.extend(hike(val+1,padded,i,j-1))
            if padded[i][j+1] == val:
                ret.extend(hike(val+1,padded,i,j+1))
            if padded[i-1][j] == val:
                ret.extend(hike(val+1,padded,i-1,j))
            if padded[i+1][j] == val:
                ret.extend(hike(val+1,padded,i+1,j))
        return ret


    ans = 0

    width = len(input[0])
    padded = []
    for line in input:
        padded.append([line[i] for i in range(width)])
        padded[-1].insert(0,-1)
        padded[-1].append(-1)
    padded.insert(0,[-1 for i in range(width+2)])
    padded.append([-1 for i in range(width+2)])

    # print(padded)

    for i in range(1,len(padded)-1):
        for j in range(1,len(padded[0])-1):
            if padded[i][j] == 0:
                trailheads = hike(1,padded,i,j)
                # print(f'trail at {i},{j} has added {trailheads} ')
                if do_part_1:
                    ans += len(set(tuple(trailheads)))
                else:
                    ans += len(trailheads)
    return ans

def process_input(filename):
    '''
    input looks like

    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732

    return input = [as-is]

    '''

    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    grid = []
    for line in lines:
        line = [int(ch) for ch in line.rstrip()]
        grid.append(line)

    return grid


if __name__ == '__main__':
    '''
    start part 1
    do_part1 returns 472 in 0.003420114517211914 seconds
    start part 2
    do_part2 returns 969 in 0.0031342506408691406 seconds
    '''
    input = process_input(INPUT)

    # print(input)
    print(f'start part 1')
    start_time = time.time()
    ans = do_part1(input);
    end_time = time.time()
    print(f'do_part1 returns {ans} in {end_time-start_time} seconds')

    # input = process_input_part2('input.txt')
    # # print(input)
    
    print(f'start part 2')
    start_time = time.time()
    ans = do_part2(input)
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

