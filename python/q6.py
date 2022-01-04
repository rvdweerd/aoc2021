import numpy as np

def GetInput(filename):
    with open(filename) as f:
        line = f.readlines()
    input = [int(str) for str in line[0].split(',')]
    return input

input=GetInput('input6.txt')
counts=np.zeros(9).astype(np.int64)
for i in input:
    counts[i]+=1
print(counts, counts.sum())
for iter in range(256):
    zeros=counts[0]
    counts[0]=counts[1]
    counts[1]=counts[2]
    counts[2]=counts[3]
    counts[3]=counts[4]
    counts[4]=counts[5]
    counts[5]=counts[6]
    counts[6]=zeros #reset after spawn
    counts[6]+=counts[7]
    counts[7]=counts[8]
    counts[8]=zeros
print(counts, counts.sum())