# https://adventofcode.com/2024/day/6
# 

import itertools
import time

def do_part2(input):
    '''
    where can you add one more obstacle to create loop?
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...

    ....#.....
    ....0>>>1#
    ....^...v.
    ..#.^...v.
    ..4>+>5#v.
    ..^.^.v.v.
    .#3<U<+<2.
    .8>>>>+9#.
    #7<<<<6v..
    ......#v..

    How many places you visit where you can execute a right turn to get back on
    prev path?

    ....#.....
    ....0>>>1#
    ....^...v.
    ..#.^...v.
    ..4>+>5#v.
    ..^.^.v.v.
    .#3XU<+<2.
    .8>>>>XX#.
    #7XX<<6v..
    ......#X..
    
    where ^ starts and turns right when hitting #

    Find "all spots where you can look at right side and see a PREV path going away from you"

    return input = [dir, pos, size, [list of obstacles]]
    '''

    return do_part1(input,False)

def do_part1(input,part1=True):
    '''
    Insight is that the ruleset is only acyclical for each line of page updates
    so for each update, generate the reduced ruleset
    flatten rules to 
    '''

    def get_to_next_obstacle(input,part1=True):
        dir_dict = {
            '^': [(-1,0),'>',set()],
            '>': [(0,1),'v',set()],
            'v': [(+1,0),'<',set()],
            '<': [(0,-1),'^',set()],
            }
        pos = input['pos']
        dir = input['dir']
        dir_dict[dir][2].add(tuple(pos))

        if part1 == False:
            new_obstacles = set()

        def part2_look_right_is_there_a_path_going_away(pos, dir, loc):
            try_pos = pos
            while True: #exit after f
                try_pos = tuple(next_step(try_pos, dir_dict[dir][0]))
                if try_pos[0] in [-1,input['size'][0]] or try_pos[1] in [-1,input['size'][1]]:
                    break
                else:
                    if try_pos in loc:
                        return True

            return False

        def next_step(pos, movement):
            return [a+b for a,b in zip(pos, movement)]

        while True:
            next_pos = next_step(pos, dir_dict[dir][0])
            # print(next_pos)
            if next_pos[0] in [-1,input['size'][0]] or next_pos[1] in [-1,input['size'][1]]:
                print(f'exiting at {pos}')
                break
            if next_pos not in input['obstacles']:
                pos = next_pos
                dir_dict[dir][2].add(tuple(pos))

                # Look to your right and see if there are prev path going away
                if part1 == False:
                    if part2_look_right_is_there_a_path_going_away(pos, dir_dict[dir][1], dir_dict[dir_dict[dir][1]][2]) == True:
                        new_obstacles.add(tuple(next_step(pos, dir_dict[dir][0])))

            else:
                # print(f'hit # @ {next_pos}, turning from {dir} to {dir_dict[dir][1]}, took {len(dir_dict[dir][2])} steps')
                dir = dir_dict[dir][1]
        # print(loc)
        if part1 == True:
            return dir_dict['^'][2] | dir_dict['>'][2] | dir_dict['v'][2] | dir_dict['<'][2]
        else:
            return new_obstacles

    return len(get_to_next_obstacle(input,part1))

def process_input(filename):
    '''
    input looks like

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...

    where ^ starts and turns right when hitting #

    return input = [dir, pos, size, [list of obstacles]]
    '''

    with open(filename,'r') as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append( [ ch for ch in line.rstrip()])
    # print(grid)

    obstacles = []
    input = {}
    input['size'] = (len(lines),len(lines[0].rstrip()))
    input['obstacles'] = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in '^>v<':
                input['dir'] = grid[i][j]
                input['pos'] = [i,j]
            elif grid[i][j] == '#':
                input['obstacles'].append([i,j])

    return input


if __name__ == '__main__':

    input = process_input('input.txt')

    # print(input)
    print(f'start part 1')
    start_time = time.time()
    ans = do_part1(input)
    end_time = time.time()
    print(f'do_part1 returns {ans} in {end_time-start_time} seconds')

    # input = process_input_part2('input.txt')
    # # print(input)
    
    print(f'start part 2')
    start_time = time.time()
    ans = do_part2(input);
    end_time = time.time()
    print(f'do_part2 returns {ans} in {end_time-start_time} seconds')

