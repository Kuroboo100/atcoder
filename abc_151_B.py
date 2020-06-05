NKM=list(map(int,input().strip().split()))
N=NKM[0]
K=NKM[1]
M=NKM[2]
A=list(map(int,input().strip().split()))

want=N*M-sum(A)

if want>K:
    print(-1)
elif want<=0:
    print(0)
else:
    print(want)

