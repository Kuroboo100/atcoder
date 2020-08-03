N,Q=map(int,input().strip().split())
S=list(input())
lr=[list(map(int,input().strip().split())) for _ in range(Q)]

#累積和
dp=[0 for _ in range(N)]
for n in range(1,len(S)):
    if S[n]=="C" and S[n-1]=="A":
        dp[n]=dp[n-1]+1
    else:
        dp[n]=dp[n-1]

#部分和の算出
for q in range(Q):
    print(dp[lr[q][1]-1]-dp[lr[q][0]-1])

