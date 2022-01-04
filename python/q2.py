import numpy as np

def GetListInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [(line.rstrip()) for line in lines]
    lines = [[i.split(' ')[0], int(i.split(' ')[1])] for i in lines]
    return lines

def part1():
    instructions=GetListInput('input2.txt')
    mapping={'forward':(1,0), 'up':(0,-1), 'down':(0,1)}
    pos=np.array([0,0])
    for i in instructions:
        pos += np.array(mapping[i[0]])*i[1]
    print(pos)
    print(np.prod(pos))

def part2():
    instructions=GetListInput('input2.txt')
    aim=0
    pos=np.array([0,0])
    for i in instructions:
        if i[0]=='down':
            aim+=i[1]
        elif i[0]=='up':
            aim-=i[1]
        elif i[0]=='forward':
            pos+=np.array([1,aim])*i[1]
    print(pos)
    print(np.prod(pos))

part2()
