# https://adventofcode.com/2024/day/2
# 

from functools import reduce
from operator import add
from collections import defaultdict

def do_part1(reports):
    '''
    for each report:
    * levels needs to increase or all decrease
    * diff of 1 to 3

    '''
    safe = 0
    for report in reports:
        if report != sorted(report) and report != sorted(report, reverse=True):
            continue
        deltas = [abs(report[i]-report[i+1]) for i in range(len(report)-1)]
        if max(deltas) < 4 and min(deltas) > 0:
            safe += 1
            # print(report)

    return safe

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

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

    return list of rows of #'s
    '''
    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    reports = [line.split() for line in lines]

    # print(list_of_pairs)

    reports = [[int(item) for item in report] for report in reports]
    # print(reports)

    return reports



if __name__ == '__main__':

    reports = process_input('input.txt')


    # print(input)
    print(f'start part 1')
    print(f'{do_part1(reports)}')

    # input = process_input_part2('input.txt')
    
    print(f'start part 2')
    print(f'{do_part2(reports)}')

