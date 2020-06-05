l=list(map(int,input().strip().split()))

for n in range(len(l)):
    for m in range(len(l)):
        if n<m and l[n]>l[m]:
            temp=l[n]
            l[n]=l[m]
            l[m]=temp
        else:
            pass
print(l[3])