import os
ROOT_DIR = os.path.abspath(os.curdir)

def GetIntInput(filename):
    with open(filename) as f:
        line = f.readlines()[0]
    line=line.strip()
    line=line.split('=')
    c1=line[1].split(',')[0].split('..')
    c2=line[2].split('..')
    xmin=int(c1[0])
    xmax=int(c1[1])
    ymin=int(c2[0])
    ymax=int(c2[1])
    return (xmin,xmax),(ymin,ymax)

def GetStationaryInitialVelocitiesX(xmin,xmax):
    dist=0
    i=0
    vinits=[]
    landings=[]
    while dist <= xmax:
        i+=1
        dist=dist+i
        if dist >= xmin and dist <= xmax:
            vinits.append(i)
            landings.append(dist)
    firstvalids=[]
    for v0 in vinits:
        p=0
        v=v0
        t=0
        while True:
            t+=1
            p+=v
            v=max(0,v-1)
            if p>=xmin and p<=xmax:
                firstvalids.append(t)
                break
    return vinits, landings, firstvalids

def GetNonStationaryInitialVelocitiesX(xmin,xmax, vxmin=0):
    vinits=[]
    landings=[]
    validtimes=[]
    for xvel0 in range(vxmin,xmax+1,1):
        t=0
        xpos=0
        xvel=xvel0
        land=[]
        validtime=[]
        vinits.append(xvel0)
        while True:
            t+=1
            xpos+=xvel
            xvel = max(0,xvel-1)
            if xpos>=xmin and xpos<=xmax:
                land.append(xpos)
                validtime.append(t)
            if xpos>xmax:
                break
        landings.append(land)
        validtimes.append(validtime)
    return vinits, landings, validtimes

def TriSum(v):
    return v*(v+1)//2

def GetTime2VelMapping(ymin,ymax):
    maxyvel = -(ymin+1)
    t2v={}
    while True:
        t=0
        ypos=0
        yvel=maxyvel
        while True:
            t+=1
            ypos+=yvel
            yvel-=1
            if ypos>=ymin and ypos<=ymax:
                if t in t2v:
                    t2v[t].append(maxyvel)
                else:
                    t2v[t]=[maxyvel]
            if ypos<ymin:
                break
        maxyvel -=1
        if maxyvel < ymin:
            break
    return t2v

def part1():
    (xmin,xmax),(ymin,ymax) = GetIntInput("input17.txt")
    stat_init_xvels, _, _ = GetStationaryInitialVelocitiesX(xmin,xmax)
    maxyvel = -(ymin+1)
    tcross = 2*maxyvel + 1
    assert tcross > max(stat_init_xvels)
    print(TriSum(maxyvel))


def part2():
    (xmin,xmax),(ymin,ymax) = GetIntInput("input17.txt")
    stat_xvinits, stat_xlandings, stat_xfirstvalids = GetStationaryInitialVelocitiesX(xmin,xmax) 
    nonstat_xvinits, nonstat_xlandings, nonstat_xvalidtimes = GetNonStationaryInitialVelocitiesX(xmin,xmax, vxmin=max(stat_xvinits)+1)
    t2v = GetTime2VelMapping(ymin,ymax)
    answerset=set()
    for i in range(len(nonstat_xvinits)):
        xvinit=nonstat_xvinits[i]
        validtimes=nonstat_xvalidtimes[i]
        for t in validtimes:
            for vy in t2v[t]:
                answerset.add((xvinit,vy))
    for j in range(len(stat_xvinits)):
        xvinit=stat_xvinits[j]
        validtimes=[q for q in range(stat_xfirstvalids[j],max(t2v.keys())+1,1)]
        for t in validtimes:
            if t in t2v:
                for vy in t2v[t]:
                    answerset.add((xvinit,vy))
    #answerlist=list(answerset)
    #answerlist.sort()
    #print(answerlist)
    print(len(answerset))

part1()
part2()
