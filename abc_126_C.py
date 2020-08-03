N,K=map(int,input().strip().split())

c=0
for n in range(1,N+1):
    if n>K:
        c+=1/N
    else:
        cnt=0
        while n<K:
            n*=2
            cnt+=1
        c+=1/N*(1/2)**cnt
print(c)


