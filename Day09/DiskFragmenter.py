# https://adventofcode.com/2024/day/9
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

    def defrag_part1(expanded):
        front = 1
        back = -1

        while (front-back) < len(expanded):
            # print(f'working through {input}')
            #move front to next empty
            front += expanded[front:].index('.')
            while (front-back) < len(expanded) and expanded[front] == '.':
                while expanded[back] == '.':
                    back -= 1
                # by now you can defrag until front isn't empty or back is
                expanded[front] = expanded[back]
                expanded[back] = '.'
                front += 1
        # print(input)

    def defrag_part2(expanded,empties,files):
        # print(expanded,empties,files)
        for file in files[::-1]:
            # find empties that fit
            file_size = file[2]
            for idx, hole in enumerate(empties):
                if file[1]<hole[0]:
                    # don't move anymore
                    break
                if hole[1] >= file_size:
                    # match! Update expanded and empties
                    # don't bother updating files
                    file_id = file[0]
                    for i in range(file_size):
                        expanded[hole[0]+i] = file_id
                        expanded[file[1]+i] = '.'
                    empties[idx][0] += file_size
                    empties[idx][1] -= file_size
                    # print(expanded, empties)
                    break

        # print(expanded)
                    
    expanded = list(input[0])
    ans = 0

    if do_part_1:
        defrag_part1(expanded)
    else:
        defrag_part2(expanded,input[1],input[2])

    
    for i,item in enumerate(expanded):
        if item != '.':
            # print(f'adding {i} * {item} to {ans}')
            ans += i*item

    return ans

def process_input(filename):
    '''
    input looks like

    2333133121414131402

    return input = [expanded list, list of empties, list of files] 
    where list of empties is a list of (idx, size of hole)
    where list of files is a list of (file_id,idx, size)

    '''

    with open(filename,'r') as f:
        lines = f.readlines()

    expanded = []
    free_space = False
    file_id = 0
    empties = []
    files = []
    for idx, digit in enumerate(lines[0].rstrip()):
        if not free_space:
            what = file_id
            files.append((file_id,len(expanded),int(digit)))
            file_id += 1
        else:
            what = '.'
            empties.append([len(expanded),int(digit)])
        free_space = not free_space
        expanded.extend([what for i in range(int(digit))])
    return [expanded,empties,files]


if __name__ == '__main__':
    '''
    start part 1
    do_part1 returns 6471961544878 in 1.4342386722564697 seconds
    start part 2
    do_part2 returns 6511178035564 in 3.0711495876312256 seconds
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

