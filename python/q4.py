import numpy as np
def GetStrInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    num_to_boards = {}
    row_counters  = []
    col_counters  = []
    lines = [(line.rstrip()) for line in lines]
    draws = lines[0].split(',')
    draws = [int(s) for s in draws]
    
    lines=lines[1:]
    boardnr=-1
    boards={}
    for i in range(len(lines)):
        if lines[i] == '':
            rownr = 0
            boardnr += 1
            boards[boardnr] = []
            row_counters.append([0]*5)
            col_counters.append([0]*5)
            continue
        row=lines[i].split()
        row=[int(n) for n in row]
        boards[boardnr].append(row)
        for colnr,number in enumerate(row):
            if number not in num_to_boards:
                num_to_boards[number] = []
            num_to_boards[number].append([boardnr, rownr, colnr, False])
        rownr += 1
    return boards, draws, num_to_boards, row_counters, col_counters

def GetFirstWinningBoard(draws, num_to_boards, row_counters, col_counters):
    draws_history = []
    marked_sets = {}
    for i in range(len(row_counters)):
        marked_sets[i] = set()
    for draw in draws:
        draws_history.append(draw)
        for board_tuple in num_to_boards[draw]:
            if board_tuple[3]==True:
                continue
            else:
                board_tuple[3]=True
                marked_sets[board_tuple[0]].add(draw)
                row_counters[board_tuple[0]][board_tuple[1]]+=1
                if row_counters[board_tuple[0]][board_tuple[1]]==5:
                    return draws_history, marked_sets, board_tuple[0]
                col_counters[board_tuple[0]][board_tuple[2]]+=1
                if row_counters[board_tuple[0]][board_tuple[2]]==5:
                    return draws_history, marked_sets, board_tuple[0]
    return draws_history, marked_sets, None

def GetWinningBoards(draws, num_to_boards, row_counters, col_counters):
    winning_boards=[]
    draws_history=[]
    marked_sets={}
    for i in range(len(row_counters)):
        marked_sets[i]=set()
    for draw in draws:
        draws_history.append(draw)
        for board_tuple in num_to_boards[draw]:
            if board_tuple[3]==True:
                continue
            else:
                board_tuple[3]=True
                marked_sets[board_tuple[0]].add(draw)
                row_counters[board_tuple[0]][board_tuple[1]]+=1
                if row_counters[board_tuple[0]][board_tuple[1]]==5:
                    if board_tuple[0] not in winning_boards:
                        winning_boards.append(board_tuple[0])
                col_counters[board_tuple[0]][board_tuple[2]]+=1
                if col_counters[board_tuple[0]][board_tuple[2]]==5:
                    if board_tuple[0] not in winning_boards:
                        winning_boards.append(board_tuple[0])
        if len(winning_boards)==len(row_counters):
            break
    return draws_history, marked_sets, winning_boards

def part1():
    print('\nSolving part1\n---------------------\n')
    boards, draws, num_to_boards, row_counters, col_counters = GetStrInput('input4.txt')
    drawsHistory, marked_sets, winningBoard = GetFirstWinningBoard(draws, num_to_boards, row_counters, col_counters)
    print('Winning board',winningBoard)
    print(boards[winningBoard])
    print('draws',drawsHistory)
    print('last draw',drawsHistory[-1])
    sum_board=np.sum(boards[winningBoard])
    sum_marked=sum(marked_sets[winningBoard])
    sum_unmarked=sum_board-sum_marked
    print('board sum',sum_board)
    print('marked sum',sum_marked)
    print('unmarked sum',sum_unmarked)
    print('Answer:',drawsHistory[-1]*sum_unmarked)

def part2():
    print('\nSolving part2\n---------------------\n')
    boards, draws, num_to_boards, row_counters, col_counters = GetStrInput('input4.txt')
    drawsHistory, marked_sets, winningBoards = GetWinningBoards(draws, num_to_boards, row_counters, col_counters)
    lwb=winningBoards[-1]
    print('Last winning board',lwb)
    print(boards[lwb])
    print('draws',drawsHistory)
    print('last draw',drawsHistory[-1])
    sum_board=np.sum(boards[lwb])
    sum_marked=sum(marked_sets[lwb])
    sum_unmarked=sum_board-sum_marked
    print('board sum',sum_board)
    print('marked sum',sum_marked)
    print('unmarked sum',sum_unmarked)
    print('Answer:',drawsHistory[-1]*sum_unmarked)

part1()
part2()