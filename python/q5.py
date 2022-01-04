import numpy as np
import math
sign = lambda x: int(math.copysign(1, x))
def GetInput(filename):
    ventlines=[]
    MINX=1e12
    MAXX=-1e12
    MINY=1e12
    MAXY=-1e12
    with open(filename) as f:
        lines = f.readlines()
    lines = [(line.rstrip().replace(' ','').split('->')) for line in lines]
    for entry in lines:
        c1=(int(entry[0].split(',')[0]),int(entry[0].split(',')[1]))
        c2=(int(entry[1].split(',')[0]),int(entry[1].split(',')[1]))
        ventlines.append(c1+c2)
        minx=min(c1[0],c2[0])
        maxx=max(c1[0],c2[0])
        miny=min(c1[1],c2[1])
        maxy=max(c1[1],c2[1])
        if minx < MINX: MINX=minx
        if miny < MINY: MINY=miny
        if maxx > MAXX: MAXX=maxx
        if maxy > MAXY: MAXY=maxy
    return ventlines, MINX, MAXX, MINY, MAXY

vlines,MINX, MAXX, MINY, MAXY=GetInput('input5.txt')
width=MAXX-MINX+1
height=MAXY-MINY+1
grid=np.zeros((height,width)).astype(np.int32)
xoffset=MINX
yoffset=MINY
numAboveTHRES=0
THRES=2
for line in vlines:
    #print(line)
    if line[0]==line[2] or line[1]==line[3]:
        for x in np.arange(min(line[0],line[2])-xoffset,max(line[0],line[2])-xoffset+1,1):
            #print('x=',x)
            for y in np.arange(min(line[1],line[3])-yoffset,max(line[1],line[3])-yoffset+1,1):
                #print('y=',y)
                grid[y,x]+=1
                if grid[y,x]==THRES:
                    numAboveTHRES+=1
    else:
        for x,y in zip(
                np.arange(line[0]-xoffset,line[2]-xoffset+sign(line[2]-line[0]),sign(line[2]-line[0])),
                np.arange(line[1]-yoffset,line[3]-yoffset+sign(line[3]-line[1]),sign(line[3]-line[1]))
            ):
            grid[y,x]+=1
            if grid[y,x]==THRES:
                numAboveTHRES+=1
print(grid.shape)
print(grid[:10,:10])
print(numAboveTHRES)
