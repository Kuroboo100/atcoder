N,M=map(int,input().strip().split())
A=list(map(int,input().strip().split()))

if sum(A)>N:
    print(-1)
else:
    print(N-sum(A))
