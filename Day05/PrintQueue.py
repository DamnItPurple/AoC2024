# https://adventofcode.com/2024/day/5
# 

import itertools
import time

def do_part2(rules,updates):
    return do_part1(rules,updates,False)

def do_part1(rules,updates,count_correct=True):
    '''
    Insight is that the ruleset is only acyclical for each line of page updates
    so for each update, generate the reduced ruleset
    flatten rules to 

    '''

    def return_middle_value(order_dict, value):
        keys = [key for key, item in order_dict.items() if item == value]
        if len(keys) != 1:
            print(f'something wrong, we found more than 1 key : {keys}')
        return keys[0]
    
    ans = 0

    for update in updates:
        reduced_rules = [item for item in rules if item[0] in update and item[1] in update ]
        flatten_rules = list(itertools.chain(*reduced_rules))
        # print(f'{len(reduced_rules)} rules are used for these pages {update}')
        pages_in_update = list(update)
        # first remove rules that don't 
        order_dict = {}
        order = 0

        #iterate and find something that's not appear on right side of rule
        while (len(pages_in_update)>0):
            for item in pages_in_update:
                try:
                    idx = flatten_rules[1::2].index(item)
                    # print(f'found {item} @ {idx}')
                except ValueError: # you are first, now remove all rules mentioning you at front
                    pages_in_update.remove(item) # don't need to check it anymore
                    order_dict[item] = order
                    order += 1
                    for i in range(len(flatten_rules)-2,-2,-2):
                        if flatten_rules[i] == item:
                            flatten_rules.pop(i)
                            flatten_rules.pop(i)
                    # print(f'---- new {flatten_rules} after removing {item}')
                    break
                    
        # print(order_dict)
        # with order_dict, convert then sort each update.  If update == sorted order, fetch it's middle #
        converted = [order_dict[item] for item in update]

        sorted_converted = sorted(converted)
        if converted == sorted_converted and count_correct == True:
            # ans += int(update[len(update)//2])
            ans += int(return_middle_value(order_dict,converted[len(update)//2]))
        elif converted != sorted_converted and count_correct == False:
            ans += int(return_middle_value(order_dict,sorted_converted[len(update)//2]))



    return ans

def process_input(filename):
    '''
    input looks like

    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47

    where page rule is a dict mapping each page to its order, starting at 0
    where updates is a list of updates
    return [page rule],update

    
    '''

    with open(filename,'r') as f:
        lines = f.readlines()
    rules = []
    for i,line in enumerate(lines):
        if len(line.rstrip()) == 0:
            lines = lines[i+1:]
            break
        else:
            rules.append(line.rstrip().split('|'))
    # print(rules)

    updates = []
    for line in lines:  # process updates
        updates.append(line.rstrip().split(','))

    # print(updates)
    return rules,updates


if __name__ == '__main__':

    rules,updates = process_input('input.txt')

    # print(input)
    print(f'start part 1')
    start_time = time.time()
    ans = do_part1(rules,updates);
    end_time = time.time()
    print(f'do_part1 returns {ans} in {end_time-start_time} seconds')

    # input = process_input_part2('input.txt')
    # # print(input)
    
    print(f'start part 2')
    start_time = time.time()
    ans = do_part2(rules,updates);
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

