import numpy as np

def printt(patch):
    for row in patch:
        s=""
        for col in row:
            if col:
                s+='#'
            else:
                s+='.'
        print(s)
    print()

def GetInput(filename):
    arr1=[]
    arr2=[]
    mode='start'
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if line=='\n':
            mode='end'
            continue
        line=line.strip()
        if mode=='start':
            for ch in line:
                if ch=='.':
                    arr1.append(0)
                else:         
                    arr1.append(1)
        else:
            tmp=[]
            for ch in line:
                if ch=='.':
                    tmp.append(0)
                else:         
                    tmp.append(1)
            arr2.append(tmp)
    return np.array(arr1).astype(np.int32), np.array(arr2).astype(np.int32)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

import copy
def ApplyConvolution(patch,iecode,padval):
    patch=np.pad(patch,3,pad_with,padder=padval)
    #printt(patch)
    target=copy.deepcopy(patch)
    m=patch.shape[0]
    n=patch.shape[1]
    for row in np.arange(1,m-1,1):
        for col in np.arange(1,n-1,1):
            if row==4 and col==4:
                k=0
            string=""
            string+=str(patch[row-1][col-1])
            string+=str(patch[row-1][col])
            string+=str(patch[row-1][col+1])
            string+=str(patch[row][col-1])
            string+=str(patch[row][col])
            string+=str(patch[row][col+1])
            string+=str(patch[row+1][col-1])
            string+=str(patch[row+1][col])
            string+=str(patch[row+1][col+1])
            index=int(string,2)
            target[row][col]=iecode[index]
    if True:#padval==0:
        k=2
        return target[k:-k,k:-k]
    else:
        return target


steps=50
iecode, patch = GetInput("input20.txt")
patch=np.pad(patch,3,pad_with,padder=0)

#printt(patch)
for i in range(steps):
    print('step ',i+1)
    padval=0
    if (i%2!=0) and iecode[0]==1 and iecode[-1]==0:
        padval=1
    patch = ApplyConvolution(patch,iecode,padval)
    #printt(patch)
print(patch.sum())
