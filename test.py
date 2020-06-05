def gcb(l):
    gcb=0
    for i in range(1,min(l)+1):
        if sum([l[n]%i for n in range(len(l))])==0:
            gcb=i
    return gcb

l=[10,15]
print(gcb(l))