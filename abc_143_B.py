N=int(input())
d=list(map(int,input().strip().split()))

SUM=0
for i in range(N-1):
    for j in range(i+1,N):
        SUM+=d[i]*d[j]

print(SUM)
        