N,M,X=map(int,input().strip().split())
C=[]
A=[]
for n in range(N):
    l=list(map(int,input().strip().split()))
    C.append(l[0])
    A.append(l[1:])

cost=sum(C)
reach=False
def dfs(L,N):
    global reach
    global cost
    if len(L)==N:
        skill=[0 for m in range(M)]
        temp=0
        for n in range(N):
            if L[n]==1:
                temp+=C[n]
                for m in range(M):
                    skill[m]+=A[n][m]
        res=True
        for e in skill:
            if e<X:
                res=False
                break
        
        if res==True:
            reach=True
            if temp<=cost:
                cost=temp     
        return
    
    else:
        for i in range(2):
            L.append(i)
            dfs(L,N)
            L.pop()

dfs([],N)
if reach==True:
    print(cost)
else:
    print(-1)
