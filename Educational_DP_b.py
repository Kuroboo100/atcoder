N,K=map(int,input().strip().split())
h=list(map(int,input().strip().split()))

inf=100000000

dp=[inf for n in range(N)]
dp[0]=0
for n in range(1,N):
    chmin=inf
    for  k in range(1,K+1):
        if n-k>=0:
            chmin=min(chmin,dp[n-k]+abs(h[n]-h[n-k]))
    dp[n]=chmin
print(dp[N-1])