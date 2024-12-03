# https://adventofcode.com/2024/day/1
# 

from functools import reduce
from operator import add
from collections import defaultdict
import re

def do_part1(pairs):
    '''
    for each pair, multiple, then sum the products

    '''

    ans = reduce(add,[item[0]*item[1] for item in pairs])

    return ans

def do_part2(reports):
    '''
    use part 1 to find failing report then use permutation to generate report with one fewer # and rerun them
    '''
    safe = 0
    for report in reports:
        if do_part1([report]) == 0:
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if do_part1([new_report]) == 0:
                    continue
                else:
                    safe+=1
                    break
        else:
            safe += 1

    return safe

def process_input(filename):
    '''
    input looks like

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    return list of tuples
    '''
    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    matches = re.findall(r'mul\(\d+,\d+\)',lines[0])
    # print(matches)
    pairs = [(int(re.findall(r'\d+',match)[0]),int(re.findall(r'\d+',match)[1])) for match in matches]
    # print(pairs)
    return pairs

def process_input_part2(filename):
    '''
    input looks like

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    return list of tuples
    '''
    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)',lines[0])
    print(matches)
    pairs = []
    skip = False
    for match in matches:
        if match[0] != 'd' and skip == False:
            pairs.append((int(re.findall(r'\d+',match)[0]),int(re.findall(r'\d+',match)[1])))
        elif match[2] == 'n':
            skip = True
        elif match[2] == '(':
            skip = False
    print(pairs)
    return pairs


if __name__ == '__main__':

    pairs = process_input('input0.txt')


    # print(input)
    print(f'start part 1')
    print(f'{do_part1(pairs)}')

    pairs = process_input_part2('input.txt')
    
    print(f'start part 2')
    print(f'{do_part1(pairs)}')

