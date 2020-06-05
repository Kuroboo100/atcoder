N,M=map(int,input().strip().split())
H=list(map(int,input().strip().split()))

A=[0 for _ in range(M)]
B=[0 for _ in range(M)]
for m in range(M):
    A[m],B[m]=map(int,input().strip().split())

R=[[] for _ in range(N)]
for i in range(M):
    R[A[i]-1].append(B[i])
    R[B[i]-1].append(A[i])

best=0
for i in range(len(R)):
    biggest=True
    if len(R[i])==0:
        pass
    else:
        for j in range(len(R[i])):
            if H[i]<=H[R[i][j]-1]:
                biggest=False
    if biggest==True:
        best+=1

print(best)
    
    
# =============================================================================
# 4 3
# 1 2 3 4
# 1 3
# 2 3
# 2 4    
# =============================================================================
# =============================================================================
# 6 5
# 8 6 9 1 2 1
# 1 3
# 4 2
# 4 3
# 4 6
# 4 6   
# =============================================================================
