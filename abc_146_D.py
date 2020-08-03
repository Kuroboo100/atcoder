import numpy as np

N=int(input())
A=[]
B=[]
for _ in range(N):
    a,b=map(int,input().strip().split())
    A.append(a)
    B.append(b)

color=1
dp=np.zeros([N,N],dtype=int32)
dp[0,0]=1

for n in range(N):
    