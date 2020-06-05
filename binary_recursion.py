N=10
a=2
m=[]
def dfs(N,a,l):
    if len(l)==N:
        l=[l[n] for n in range(len(l))]
        m.append(l)
    else:
        for n in range(a):
            l.append(n)
            dfs(N,a,l)
            l.pop()

def dfs2(N,M,l):
    if len(l)==N:
        l=[l[n] for n in range(len(l))]
        m.append(l)
    else:
        if len(l)==0:
            for n in range(M):
                l.append(n)
                dfs(N,M,l)
                l.pop()
        else:
            prev_max=l[-1]
            for n in range(prev_max,M):
                l.append(n)
                dfs(N,M,l)
                l.pop()

dfs2(3,5,[])
print(*m,sep="\n")

            

