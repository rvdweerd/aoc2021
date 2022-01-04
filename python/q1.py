import numpy as np

def GetIntInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]
    return lines

def GetNumIncr(seq):
    count=0
    for i in range(len(seq)-1):
        if seq[i+1] > seq[i]:
            count+=1
    return count

lines=GetIntInput('input1.txt')
print(GetNumIncr(lines))

y=np.convolve(lines,[1,1,1],mode='valid')
print(GetNumIncr(y))