# https://adventofcode.com/2024/day/7
# 

from functools import reduce
import itertools
import time

INPUT = 'input.txt'

def do_part2(equations):
    return do_part1(equations, True)

def do_part1(equations, do_part_2 = False):
    '''
    series of equations, returning sum of equations that work

    '''
    ans = 0

    def solve(operands, code):
        '''
        0 is +, 1 is *
        '''
        # print(operands, code)
        ans = operands[0]
        for i,item in enumerate(operands[1:]):
            if code % 2:
                ans += item
            else:
                ans *= item
            code = code >> 1
        # print(ans)

        return ans

    if do_part_2:
        unsolveds = []

    for equ in equations:
        found = False
        for op_combo in range(pow(2,len(equ[1])-1)):
            if equ[0] == solve(equ[1], op_combo):
                ans += equ[0]
                found = True
                break
        if found == False and do_part_2:
            unsolveds.append(equ)

    if do_part_2:
        def solve_with_concat(operands, code):
            '''
            0 is +, 1 is *, 2 is concat
            '''
            # print(operands, code)
            ans = operands[0]
            for i,item in enumerate(operands[1:]):
                if code % 3 == 0:
                    ans += item
                elif code % 3 == 1:
                    ans *= item
                elif code % 3 == 2:
                    ans = int(str(ans) + str(item))
                code = code // 3
            # print(f'\t gives {ans}')

            return ans

        print(f'I have {len(unsolveds)} equations to go through')
        for uns in unsolveds:
            found = False
            for op_combo in range(pow(3,len(uns[1])-1)):
                if uns[0] == solve_with_concat(uns[1], op_combo):
                    ans += uns[0]
                    found = True
                    break


    return ans

def process_input(filename):
    '''
    input looks like

    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20

    return [result, (operands)]

    '''

    with open(filename,'r') as f:
        lines = f.readlines()
    equations = []
    for line in lines:
        equ = line.rstrip().split()
        # print(equ)
        equations.append((int(equ[0][:-1]),[int(item) for item in equ[1:]]))

    # print(equations)
    return equations


if __name__ == '__main__':
    '''
    $ python BridgeRepair.py 
    start part 1
    do_part1 returns 4555081946288 in 0.404141902923584 seconds
    start part 2
    I have 440 equations to go through
    do_part2 returns 227921760109726 in 27.367647647857666 seconds
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
    ans = do_part2(input);
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

