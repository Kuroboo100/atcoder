N,M,K=map(int,input().strip().split())
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))

a=[0]
b=[0]
for n in range(N):
    a.append(a[n]+A[n])
for m in range(M):
    b.append(b[m]+B[m])

num=0
bmax=M+1
for n in range(N+1):
    if a[n]>K:
        break
    for m in reversed(range(bmax)):
        if b[m]<=K-a[n]:
            num=max(num,n+m)
            bmax=m+1
            break
print(num)



    
