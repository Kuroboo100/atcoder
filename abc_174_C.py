K=int(input())
    
a=7%K
i=1
dp=[0 for n in range(K)]
dp[a]=1
    
while a!=0:
    a=(10*a+7%K)%K
    if dp[a]==0:
        dp[a]+=1
        i+=1
    else:
        print(-1)
        break
else:
    print(i)