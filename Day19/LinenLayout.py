# https://adventofcode.com/2024/day/19
# 

from functools import reduce
import itertools
import time
from collections import defaultdict

INPUT = 'input.txt'

def do_part2(input):
    return do_part1(input, False)

rejected_set = set()
ways_dict = dict()

def add_to_rejected(pattern):
    rejected_set.add(pattern)
    # pass

def rejected(pattern):
    if pattern in rejected_set:
        return True
    else:
        return False

def do_part1(input, do_part_1 = True):
    '''
    return sum of product

    '''
    towels = input[0]
    early_term = do_part_1
    ans = 0
    def composable(pattern, arrangement: list ):
        pattern_len = len(pattern)
        if pattern_len == 0:
            # print(f'{arrangement}')
            return 1
        if rejected(pattern):
            return 0
        if pattern in ways_dict:
            return ways_dict[pattern]
        # if pattern_len == 1:
        #     if pattern in towels:
        #         return 1
        #     else:
        #         return 0
        works = 0
        for towel in towels:
            towel_len = len(towel)
            if towel_len <= pattern_len and towel == pattern[:towel_len]:
                shortened = pattern[towel_len:]
                ways = composable(shortened, arrangement + [towel])
                works += ways
                if ways == 0:
                    add_to_rejected(shortened)
                elif early_term == True:
                    return works
                elif shortened not in ways_dict:
                    ways_dict[shortened] = ways

        return works
                
    for pattern in input[1]:
        # print(f'this pattern {pattern}')
        ways = composable(pattern, [])
        # print(f'{ways}.', end='')
        ans += ways
        # print(f'after {pattern} new {ans}')

    return ans

def process_input(filename):
    '''
    input looks like

    r, wr, b, g, bwu, rb, gb, br

    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb

    return input = [{towels as set of strings}, [list of patterns as strings]]

    '''

    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    towels = set(lines[0].rstrip().split(', '))
    patterns = []
    for line in lines[2:]:
        patterns.append(line.rstrip())

    return (towels,patterns)


if __name__ == '__main__':
    '''
    $ python LinenLayout.py 
    start part 1
    do_part1 returns 242 in 0.13075828552246094 seconds
    start part 2
    do_part2 returns 595975512785325 in 0.9117319583892822 seconds

    Until I started using ways_dict, part2 is extremely slow.
    rejected_set has very minor effect on speedup
    '''
    input = process_input(INPUT)

    # print(input)
    print(f'start part 1')
    start_time = time.time()
    ans = do_part1(input)
    end_time = time.time()
    print(f'do_part1 returns {ans} in {end_time-start_time} seconds')

    # input = process_input_part2('input.txt')
    # print(input)
    
    print(f'start part 2')
    start_time = time.time()
    ans = do_part2(input)
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

