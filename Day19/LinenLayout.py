# https://adventofcode.com/2024/day/19
# 

from functools import reduce
import itertools
import time
from collections import defaultdict

INPUT = 'input0.txt'

def do_part2(input):
    return do_part1(input, False)

def do_part1(input, do_part_1 = True):
    '''
    return sum of product

    '''
    ans = 0
    def composable(towels, pattern, early_term):
        # if len(pattern) == 0:
        #     return 1
        # if len(pattern) == 1:
        #     if pattern in towels:
        #         return 1
        #     else:
        #         return 0
        works = 0
        for towel in towels:
            if towel == pattern:
                return 1
            if len(towel) < len(pattern) and towel == pattern[:len(towel)]:
                shortened = pattern[len(towel):]
                works += composable(towels, shortened, early_term)
                if works == 0:
                    continue
                elif early_term == True:
                    return works
        

        return works
                
    for pattern in input[1]:
        ans += composable(input[0], pattern, do_part_1)
        print(f'after {pattern} new {ans}')

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
    start part 1
    do_part1 returns 472 in 0.003420114517211914 seconds
    start part 2
    do_part2 returns 969 in 0.0031342506408691406 seconds
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

