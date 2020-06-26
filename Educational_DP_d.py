def main():#TLE
    N,W=map(int,input().strip().split())
    l=[]
    for n in range(N):
        l.append(list(map(int,input().strip().split())))

    dp=[[0 for w in range(W+1)] for n in range(N+1)]
    for n in range(1,N+1):
        for i in range(W+1):
            #各nにつき重みiを超えない最大値を求める
            tmp=l[n-1][0]
            if  tmp+i<=W:
                dp[n][tmp+i]=max(dp[n][tmp+i],dp[n-1][i]+l[n-1][1])
            dp[n][i]=max(dp[n][i],dp[n-1][i])

    res=0
    for i in range(W+1):
        res=max(res,dp[N][i])

    print(res)

import numpy as np

def main_():
    N,W=map(int,input().strip().split())
    l=[]
    for n in range(N):
        l.append(list(map(int,input().strip().split())))
    
    dp=np.zeros(W+1,np.int64)

    for n in range(N):
        w=l[n][0]
        v=l[n][1]
        dp[w:]=np.maximum(dp[w:],dp[:-w]+v)
    return dp.max()

if __name__=="__main__":
    print(main_())


