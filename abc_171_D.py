N=int(input())
A=list(map(int,input().strip().split()))
Q=int(input())

dp=[0 for n in range(100000+1)]
for n in range(len(A)):
    dp[A[n]-1]+=1

init=0
for n in range(1,len(dp)):
    init+=n*dp[n-1]

ans=init
for n in range(Q):
    B,C=map(int,input().strip().split())
    ans=ans-dp[B-1]*B+dp[B-1]*C
    dp[C-1]+=dp[B-1]
    dp[B-1]=0
    print(ans)
