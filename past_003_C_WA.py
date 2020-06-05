#1例だけWA
import math

A,R,N=map(int,input().strip().split())

INF=1000000000

LARGE=1
def rec(R,n):
    global LARGE
    LARGE*=R
    if LARGE>INF:
        print("large")
        return 0
    else:
        if n==1:
            return R
        else:
            if n%2==0:
                return pow(rec(R,n//2),2)
            else:
                return R*pow(rec(R,(n-1)//2),2)

ans=rec(R,N-1)*A

if ans!=0:
    if ans>INF:
        print("large")
    else:
        print(ans)