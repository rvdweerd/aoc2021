import numpy as np
def GetStrInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [(line.rstrip()) for line in lines]
    return lines

def ConvertToNumpy(input):
    output=[]
    for binstr in input:
        binarr=[]
        for bindig in binstr:
            binarr.append(int(bindig))
        output.append(binarr)
    return np.array(output)

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n

def part1():
    input=GetStrInput('input3.txt')
    input=ConvertToNumpy(input)
    bin_np=(input.sum(axis=0)/input.shape[0]>0.5).astype(np.int32)
    bin_str=''#'0b'
    for b in bin_np:
        bin_str+=str(b)
    print(bin_str)
    val=int(bin_str,2)
    not_val=bit_not(val,len(bin_str))

    print(bin(val),val)
    print(bin(not_val),not_val)
    print(val*not_val)

def GetFilteredNumber(input, keep=1):
    for i in range(input.shape[1]):
        oneShare = input[:,i].sum(axis=0)/input.shape[0]
        if oneShare<0.5:
            # keep entries with bit 0
            select=input[:,i]==1-keep
            input=input[select]
        elif oneShare>=0.5:
            select=input[:,i]==keep
            input=input[select]
        if len(input)==1:
            bin_str=''#'0b'
            for b in input.squeeze():
                bin_str+=str(b)
            print(bin_str)
            val=int(bin_str,2)
            return val
    return None

def part2():
    input=GetStrInput('input3.txt')
    input=ConvertToNumpy(input)
    valA=GetFilteredNumber(input,1)
    valB=GetFilteredNumber(input,0)
    print(valA*valB)

part2()