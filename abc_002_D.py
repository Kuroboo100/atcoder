N,M=map(int,input().strip().split())
xy=[list(map(int,input().strip().split())) for m in range(M)]

max_num=1
def dfs(l,N,xy,M):
    global max_num
    num=0
    party=True
    belong=[]
    if len(l)==N:
        for n in range(N):
            if l[n]==1:
                belong.append(n+1)
                num+=1
        if len(belong)>=2:
            for i in range(len(belong)-1):
                for j in range(i+1,len(belong)):
                    if [belong[i],belong[j]] not in xy and [belong[j],belong[i]] not in xy:
                        party=False
                        break
        if party==True:
            max_num=max(num,max_num)
        return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,N,xy,M)
            l.pop()
dfs([],N,xy,M)
print(max_num)
        

