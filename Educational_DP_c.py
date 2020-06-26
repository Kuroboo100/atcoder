N=int(input())
l=[]
for n in range(N):
    l.append(list(map(int,input().strip().split())))
    
dp=[[0,0,0] for n in range(N)]
dp[0]=l[0]
for n in range(1,N):
    for i in range(3):
        for j in range(3):
            if i!=j:
                dp[n][i]=max(dp[n][i],dp[n-1][j]+l[n][i])
print(max(dp[N-1]))
