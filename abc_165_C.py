N,M,Q=map(int,input().strip().split())

l=[]
for n in range(Q):
    l.append(list(map(int,input().strip().split())))

def score(A):
    SUM=0
    for i in range(Q):
        if A[l[i][1]]-A[l[i][0]]==l[i][2]:
            SUM+=l[i][3]
    return SUM    

ans=0
def dfs(A,N,M):
    if len(A)==N+1:
        global ans
        ans=max(ans,score(A))
        return
    else:
        last=A[-1]
        for n in range(last,M+1):
            A.append(n)
            dfs(A,N,M)
            A.pop()

dfs([1],N,M)
print(ans)
        

