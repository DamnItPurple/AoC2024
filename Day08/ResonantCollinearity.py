# https://adventofcode.com/2024/day/8
# 

from functools import reduce
import itertools
import time
from collections import defaultdict

INPUT = 'input.txt'

def do_part2(input):
    return do_part1(input, True)

def do_part1(input, harmonics = False):
    '''
    return How many unique locations within the bounds of the map contain an antinode?

    '''

    def add_antinodes(coords,grid_size, harmonics):
        def all_combo(coords):
            for i in range(len(coords)-1):
                for j in range(i+1,len(coords)):
                    yield (coords[i],coords[j])

        def get_aa(pair, harmonics, grid_size):
            def bounds_check(pos, grid_size):
                if pos[0] < 0 or pos[0] >= grid_size[0] or pos[1] < 0 or pos[1] >= grid_size[1]:
                    return False
                else:
                    return True
                
            delta = (pair[0][0]-pair[1][0],pair[0][1]-pair[1][1])

            aa1 = (pair[0][0]+delta[0],pair[0][1]+delta[1])
            aa2 = (pair[1][0]-delta[0],pair[1][1]-delta[1])
            aas = []
            for aa in [aa1,aa2]:
                if bounds_check(aa, grid_size) == True:
                    aas.append(aa)
            if harmonics == False:
                return aas
            else:
                harmonic_aas = [pair[0],pair[1]]
                while True:
                    if bounds_check(aa1, grid_size) == True:
                        harmonic_aas.append(aa1)
                        aa1 = (aa1[0]+delta[0],aa1[1]+delta[1])
                    else:
                        break
                while True:
                    if bounds_check(aa2, grid_size) == True:
                        harmonic_aas.append(aa2)
                        aa2 = (aa2[0]-delta[0],aa2[1]-delta[1])
                    else:
                        break
                return harmonic_aas

        ans = set()

        for pair in all_combo(coords):
            aas = get_aa(pair, harmonics, grid_size)
            # print(f'{len(aas)} for {pair}, to be added to {len(ans)}: {aas}')
            ans = ans | set(tuple(aas))
        return ans

    ans = set()

    grid_size = input[0]

    # for each key, find pairwise antinode and store them in set
    for key in input[1]:
        # print(f'{key}')
        ans = ans | add_antinodes(input[1][key], grid_size, harmonics)

    return len(ans)

def process_input(filename):
    '''
    input looks like

    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............

    return input = [(size of grid),dict of antennas and their locations]

    '''

    with open(filename,'r') as f:
        lines = f.readlines()

    ann_dict = defaultdict(list)

    for i,line in enumerate(lines):
        for j,item in enumerate(line.rstrip()):
            spot = lines[i][j]
            if spot != '.':
                ann_dict[spot].append((i,j))

    # print(ann_dict)
    return ((len(lines),len(lines[0].rstrip())),ann_dict)


if __name__ == '__main__':
    '''
    EVEN THOUGH I got the right answer for part 2, I did not implement
    "an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance."
    I just got lucky with the data set.  Imagine if 2 antennas are exactly (2,2) apart, I think I would not get it right

    $ python ResonantCollinearity.py 
    start part 1
    do_part1 returns 276 in 0.0010063648223876953 seconds
    start part 2
    do_part2 returns 991 in 0.0018639564514160156 seconds
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

