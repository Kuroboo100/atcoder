N=int(input())
X=list(map(int,input().strip().split()))

def min_energy(N,X):
    min_e=100000000
    for l in range(max(X)+1):
        e=0
        for n in range(N):
            e+=(X[n]-l)**2
        if min_e>=e:
            min_e=e
    return min_e

print(min_energy(N,X))



