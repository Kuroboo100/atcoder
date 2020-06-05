N,M=map(int,input().strip().split())
k=[]
s=[]
for m in range(M):
    ks=list(map(int,input().strip().split()))
    k.append(ks[0])
    s.append(ks[1:])
p=list(map(int,input().strip().split()))

def judge(k,s,p,l):
    ON=True
    for m in range(M):
        num=0
        for i in range(k[m]):
            if l[s[m][i]-1]==1:
                num+=1
        if num%2!=p[m]:
            ON=False
            break
    return ON             
                
cnt=0
def dfs(l,N,M):
    global cnt
    if len(l)==N:
        if judge(k,s,p,l):
            cnt+=1            
        return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,N,M)
            l.pop()

dfs([],N,M)
print(cnt)