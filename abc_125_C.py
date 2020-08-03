N=int(input())
A=list(map(int,input().strip().split()))

def gcd(C,D):
    a=min([C,D])
    b=max([C,D])
    tmp=a
    a=b%a
    b=tmp
    if a==0:
        return tmp
    else:
        return gcd(a,b)

g=gcd(A[0],A[1])
for n in range(2,N):
    g=gcd(g,A[n])

print(g)
