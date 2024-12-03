# https://adventofcode.com/2024/day/1
# 

from functools import reduce
from operator import add
from collections import defaultdict

def do_part1(nums1, nums2):
    '''

    '''
    deltas = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2) ]
    return reduce(add, deltas)

def do_part2(nums1, nums2):
    '''
    nums2 needs to be transformed to dict for similarity score
    '''
    n2_dict = {num: nums2.count(num) for num in set(nums2)}
    # print(n2_dict)
    n2_dict = defaultdict(int,n2_dict)
    similarity_score = [n2_dict[n1] * n1 for n1 in nums1 ]
    return reduce(add, similarity_score)

def process_input(filename):
    '''
    input looks like

    3   4
    4   3
    2   5

    return 2 sorted list of numbers from smallest to largest
    '''
    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    list_of_pairs = [line.split() for line in lines]

    # print(list_of_pairs)

    list1 = [int(item[0]) for item in list_of_pairs]
    # print(list1)
    list2 = [int(item[1]) for item in list_of_pairs]
    print(list1, list2)

    return list1, list2



if __name__ == '__main__':

    list1, list2 = process_input('input.txt')


    # print(input)
    print(f'start part 1')
    print(f'{do_part1(sorted(list1), sorted(list2))}')

    # input = process_input_part2('input.txt')
    
    print(f'start part 2')
    print(f'{do_part2(list1,list2)}')

