import math

n,a,b=map(int,input().strip().split())

ANS=2**n-1
MOD=10**9+7

def C(x,n):
    i=1
    top=n
    bottom=1
    while i<x:
        top*=(n-i)
        bottom*=i+1
        i+=1
    return top//bottom

print(ANS%MOD-C(a,n)%MOD-C(b,n)%MOD)