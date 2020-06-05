from collections import deque

def bfs2(g,n,m):
    pre=[0 for _ in range(n+1)]
    pre[1]=1
    q=deque([1])
    while q:
        x=q.popleft()
        for i in range(len(g[x])):
            if pre[g[x][i]]==0:
                q.append(g[x][i])
                pre[g[x][i]]=x
    return pre

def main2():
    #normal input
    n,m=map(int,input().strip().split())
    g=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().strip().split())
        g[a].append(b)
        g[b].append(a)
        
    pre=bfs2(g,n,m)
    
    print("Yes" if 0 not in pre[1:] else "No")
    for i in range(2,len(pre)):
        print(pre[i])

if __name__=="__main__":
    main2()