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
    
    print("yes" if 0 not in pre[1:] else "No")
    for i in range(2,len(pre)):
        print(pre[i])

if __name__=="__main__":
    main2()

#5/17 TLE--------------------------------------------------------------
def bfs(AB,N,M):
    #initialize route guide
    g=[0 for n in range(N)]
    g[0]=1
    
    q=deque([1])
    while q:
        x=q.popleft()
        for m in range(M):
            if AB[m][0]==x and g[AB[m][1]-1]==0:
                q.append(AB[m][1])
                g[AB[m][1]-1]=x
            elif AB[m][1]==x and g[AB[m][0]-1]==0:
                q.append(AB[m][0])
                g[AB[m][0]-1]=x
    ok=True if 0 not in g else False
    return ok,g
    
def main():
    #normal input
    N,M=map(int,input().strip().split())
    AB=[list(map(int,input().strip().split())) for _ in range(M)]
    
    ok,g=bfs(AB,N,M)
    
    print("Yes" if ok else "No")
    if ok:
        for n in range(1,N):
            print(g[n]) 
    return

#if __name__=="__main__":
#    main()
