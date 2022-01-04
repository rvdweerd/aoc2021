import numpy as np

def GetStrInput(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [(line.rstrip().split(' ')) for line in lines]
    notes = [line[:10] for line in lines]
    obs = [line[11:] for line in lines]
    return notes, obs

def GetMappings():
    numsegs_per_digit = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    numsegs_to_digits = {}
    for k,v in numsegs_per_digit.items():
        if v not in numsegs_to_digits:
            numsegs_to_digits[v]=[]
        numsegs_to_digits[v].append(k)
    return numsegs_per_digit, numsegs_to_digits

notes, outputs = GetStrInput('input8.txt')
nseg_per_digit, nseg_to_digits = GetMappings()
unique_num_segments=set([2,3,4,7])

count=0
for output in outputs:
    for str in output:
        if len(str) in unique_num_segments:
            count+=1
print(count)