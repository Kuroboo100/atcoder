N,K=map(int,input().strip().split())
A=list(map(int,input().strip().split()))
for k in range(K,N):
    if A[k]/A[k-K]>1:
        print("Yes")
    else:
        print("No")
