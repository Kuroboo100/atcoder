N,K,Q=map(int,input().strip().split())
A=[int(input()) for _ in range(Q)]

dp=[0 for _ in range(N)]
for n in range(Q):
    dp[A[n]-1]+=1

for n in range(N):
    if dp[n]+K-Q>0:
        print("Yes")
    else:
        print("No")
