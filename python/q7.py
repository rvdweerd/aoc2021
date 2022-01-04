import numpy as np
import matplotlib.pyplot as plt

def GetInput(filename):
    with open(filename) as f:
        line = f.readlines()
    input = [int(str) for str in line[0].split(',')]
    return np.array(input), min(input), max(input)

def part1():
    crabs_pos, xmin, xmax=np.array(GetInput('input7.txt'))
    x=np.arange(xmin,xmax+1,1)[:,np.newaxis]
    X=np.tile(crabs_pos,(len(x),1))
    X_1norm=np.linalg.norm(X-x,ord=1,axis=1)
    i=np.argmin(X_1norm)
    print('Best position:', x[i])
    print('Fuel spent:', X_1norm[i])
    plt.plot(x,X_1norm)
    plt.savefig('q7_part1.png')

def CreateLookupTable(maxdist):
    mapping={0:0}
    for i in range(maxdist):
        mapping[i+1]=mapping[i]+i+1
        mapping[-i-1]=mapping[i+1]
    return mapping


def part2():
    crabs_pos, xmin, xmax=np.array(GetInput('input7.txt'))
    x=np.arange(xmin,xmax+1,1)[:,np.newaxis]
    X=np.tile(crabs_pos,(len(x),1))
    D=X-x
    maxdist=np.max(np.abs(D))
    weighted_dist=CreateLookupTable(maxdist)
    print(D.shape)
    for row in range(D.shape[0]):
        D[row] = [weighted_dist[k] for k in D[row].tolist()]
    X_1norm=np.linalg.norm(D,ord=1,axis=1)
    i=np.argmin(X_1norm)
    print('Best position:', x[i])
    print('Fuel spent:', X_1norm[i])
    plt.plot(x,X_1norm)
    plt.savefig('q7_part2.png')

part2()