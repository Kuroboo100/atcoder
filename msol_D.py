N=int(input())
A=list(map(int,input().strip().split()))
money=1000
stock=0
for n in range(N):
    if n<N-1:
        if A[n]<A[n+1]:
            if money>=A[n]:
                stock+=money//A[n]
                money%=A[n]
        else:
            money+=A[n]*stock
            stock=0
    else:
        money+=A[n]*stock
print(money)