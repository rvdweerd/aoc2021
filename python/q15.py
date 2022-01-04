from queue import PriorityQueue
import numpy as np

def GetIntInput(filename):
    gridc=[]
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = [int(i) for i in line.strip()]
        gridc.append(line)
    gridc=np.array(gridc)
    h=gridc.shape[0]
    w=gridc.shape[1]
    N=w*h
    return gridc, (w,h,N)

def BuildGraph(gridc, w, h):
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    gridn={}
    neighborsn={}
    for y in range(h):
        for x in range(w):
            n=x+y*w
            gridn[n]=gridc[y][x]
            for d in directions:
                newx=x+d[0]
                newy=y+d[1]
                if newx>=0 and newx<w and newy>=0 and newy <h:
                    newn=newx+newy*w
                    if n in neighborsn:
                        neighborsn[n].append(newn)
                    else:
                        neighborsn[n]=[newn]
    return gridn, neighborsn


def FindShortestPath(startnode, targetnode, costn, neighborsn):
    pqueue=PriorityQueue()
    visited=set([startnode])
    pqueue.put((0,[startnode]))
    while not pqueue.empty():
        nextobj = pqueue.get()
        path_sofar = nextobj[1]
        cost_sofar = nextobj[0]
        curr_node = path_sofar[-1]
        if curr_node == targetnode:
            return path_sofar, cost_sofar
        for n in neighborsn[curr_node]:
            if n in visited:
                continue
            visited.add(n)
            totalcost = cost_sofar + costn[n]
            pqueue.put((totalcost, path_sofar+[n]))

def ExpandGrid(grid, w,h,N):
    gridXL=grid
    for i in range(2):
        grid1=(gridXL+1)%10
        grid1[(gridXL+1)%10==0]=1
        grid2=(grid1+1)%10
        grid2[(grid1+1)%10==0]=1
        grid3=(grid2+1)%10
        grid3[(grid2+1)%10==0]=1
        grid4=(grid3+1)%10
        grid4[(grid3+1)%10==0]=1
        gridXL=np.concatenate((gridXL,grid1,grid2,grid3,grid4),axis=i)
    hXL=gridXL.shape[0]
    wXL=gridXL.shape[1]
    NXL=hXL*wXL
    return gridXL, (wXL,hXL,NXL)

def part1():
    gridc, (w,h,N) = GetIntInput('input15.txt')
    costn, neighborsn = BuildGraph(gridc, w, h)
    spath, cost = FindShortestPath(0,N-1,costn, neighborsn)
    print(spath,cost)

def part2():
    gridc, (w,h,N) = GetIntInput('input15.txt')
    gridcXL, (wXL, hXL, NXL) = ExpandGrid(gridc, w,h,N)
    costn, neighborsn = BuildGraph(gridcXL, wXL, hXL)
    spath, cost = FindShortestPath(0,NXL-1,costn, neighborsn)
    print(spath,cost)


part2()