# https://adventofcode.com/2024/day/4
# 

def match(grid, i, j):
    '''
    within grid, find 0 then search for complete phrase

    same row:  left or right
    same col: up or down
    diag: 4 ways
    '''
    NUM = [0,1,2,3]
    num = 0
    # row
    if grid[i][j:j+len(NUM)] == NUM:
        num += 1
    if grid[i][j:j-len(NUM):-1] == NUM:
        num += 1
    # col
    up = [grid[i][j], grid[i-1][j], grid[i-2][j], grid[i-3][j]]
    down = [grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]
    if up == NUM:
        num += 1
    if down == NUM:
        num += 1
    NE = [grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]]
    SE = [grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]
    SW = [grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]]
    NW = [grid[i][j], grid[i-1][j-1], grid[i-2][j-2], grid[i-3][j-3]]
    if NE == NUM:
        num += 1
    if SE == NUM:
        num += 1
    if SW == NUM:
        num += 1
    if NW == NUM:
        num += 1
    return num

def do_part1(grid):
    '''
    within grid, find 0 then search for complete phrase

    same row:  left or right
    same col: up or down
    diag: 4 ways

    '''
    ans = 0

    for i in range(3, len(grid)-3):
        for j in range(3, len(grid[0])-3):
            if grid[i][j] != 0:
                continue
            else:
                ans += match(grid, i, j)


    return ans

def process_input(filename):
    '''
    input looks like

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX

    return replacing X=0, M=1, A=2, S=3

    '''

    PHRASE = 'XMAS'

    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    grid = []
    for line in lines:
        line = [PHRASE.find(ch)  for ch in line.rstrip()]
        grid.append(line)

    padded_grid = [[6,5,4] + line + [4,5,6] for line in grid]
    padded_grid.insert(0,[4]*len(padded_grid[0])) 
    padded_grid.insert(0,[5]*len(padded_grid[0])) 
    padded_grid.insert(0,[6]*len(padded_grid[0])) 
    padded_grid.append([4]*len(padded_grid[0])) 
    padded_grid.append([5]*len(padded_grid[0])) 
    padded_grid.append([6]*len(padded_grid[0])) 

    return padded_grid

def process_input_part2(filename):
    '''
    input looks like

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX

    return replacing M=0, A=1, S=2

    '''
    PHRASE_2 = 'MAS'

    with open(filename,'r') as f:
        lines = f.readlines() # each line is a pair of tokens separated by whitespace

    grid = []
    for line in lines:
        line = [PHRASE_2.find(ch)  for ch in line.rstrip()]
        grid.append(line)

    padded_grid = [[4] + line + [4] for line in grid]
    padded_grid.insert(0,[4]*len(padded_grid[0])) 
    padded_grid.append([4]*len(padded_grid[0])) 

    return padded_grid


def match_part2(grid, i, j):
    '''
    within grid, find 1 ('A') then search for X pattern

    '''
    NUM_2 = [0,2,0,2]
    num = 0
    NWNE = [grid[i-1][j-1], grid[i+1][j+1], grid[i-1][j+1], grid[i+1][j-1]]
    NWSW = [grid[i-1][j-1], grid[i+1][j+1], grid[i+1][j-1], grid[i-1][j+1]]
    SESW = [grid[i+1][j+1], grid[i-1][j-1], grid[i+1][j-1], grid[i-1][j+1]]
    SENE = [grid[i+1][j+1], grid[i-1][j-1], grid[i-1][j+1], grid[i+1][j-1]]
    if NWNE == NUM_2:
        num += 1
    if NWSW == NUM_2:
        num += 1
    if SESW == NUM_2:
        num += 1
    if SENE == NUM_2:
        num += 1
    return num

def do_part2(grid):
    '''
    within grid, find 1 then search for X pattern

    '''
    ans = 0

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] != 1:
                continue
            else:
                ans += match_part2(grid, i, j)


    return ans



if __name__ == '__main__':

    input = process_input('input.txt')

    # print(input)
    print(f'start part 1')
    print(f'{do_part1(input)}')

    input = process_input_part2('input.txt')
    # print(input)
    
    print(f'start part 2')
    print(f'{do_part2(input)}')

