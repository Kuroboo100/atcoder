N,K=map(int,input().strip().split())

l=[n for n in range(1,N+1)]
for n in range(K):
    d=int(input())
    A=list(map(int,input().strip().split()))
    for n in range(d):
        if A[n] in l:
            l.remove(A[n])

print(len(l))

        
    