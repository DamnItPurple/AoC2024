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

    def defrag_part1(input):
        front = 1
        back = -1

        while (front-back) < len(input):
            # print(f'working through {input}')
            #move front to next empty
            front += input[front:].index('.')
            while (front-back) < len(input) and input[front] == '.':
                while input[back] == '.':
                    back -= 1
                # by now you can defrag until front isn't empty or back is
                input[front] = input[back]
                input[back] = '.'
                front += 1
        # print(input)

    def defrag_part2(input):
        front = 1
        back = -1

        while (front-back) < len(input):
            # print(f'working through {input}')
            #move front to next empty
            front += input[front:].index('.')
            while (front-back) < len(input) and input[front] == '.':
                while input[back] == '.':
                    back -= 1
                # by now you can defrag until front isn't empty or back is
                input[front] = input[back]
                input[back] = '.'
                front += 1
        # print(input)

    ans = 0

    if do_part_1:
        defrag_part1(input)
    else:
        defrag_part2(input)

    
    for i,item in enumerate(input):
        if item != '.':
            # print(f'adding {i} * {item} to {ans}')
            ans += i*item

    return ans

def process_input(filename):
    '''
    input looks like

    2333133121414131402

    return input = [expanded list]

    '''

    with open(filename,'r') as f:
        lines = f.readlines()

    expanded = []
    free_space = False
    file_id = 0
    for digit in lines[0].rstrip():
        if not free_space:
            what = file_id
            file_id += 1
        else:
            what = '.'
        free_space = not free_space
        expanded.extend([what for i in range(int(digit))])
    # print(ann_dict)
    return expanded


if __name__ == '__main__':
    '''
    start part 1
    do_part1 returns 6471961544878 in 2.1512091159820557 seconds
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
    
    # print(f'start part 2')
    # start_time = time.time()
    # ans = do_part2(input)
    # end_time = time.time()
    # print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

