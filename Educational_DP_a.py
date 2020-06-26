import sys
sys.setrecursionlimit(200000)

def dp_func(n,dp,h):
    if n==0:
        return 0
    elif n==1:
        return dp[1]
    
    else:
        if dp[n-1]==-1:
            dp[n-1]=dp_func(n-1,dp,h)

        c1=dp[n-1]+abs(h[n]-h[n-1])

        if dp[n-2]==-1:
            dp[n-2]=dp_func(n-2,dp,h)
            
        c2=dp[n-2]+abs(h[n]-h[n-2])
        
        dp[n]=min(c1,c2)
        return dp[n]

def main():
    #input
    N=int(input())
    h=list(map(int,input().strip().split()))
    # N=10000
    # h=[n**2 for n in range(N)]

    dp=[-1 for n in range(N)]
    dp[0]=0
    dp[1]=abs(h[1]-h[0])

    return dp_func(N-1,dp,h)

if __name__=="__main__":
    print(main())

