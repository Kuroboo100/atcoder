N=int(input())
t=[int(input()) for _ in range(N)]

min_time=0
for n in range(N):
    min_time+=t[n]
    
def dfs(l,N,t):
    global min_time
    g1=0
    g2=0
    if len(l)==N:
        for n in range(N):
            if l[n]==0:
                g1+=t[n]
            else:
                g2+=t[n]
        min_time=min(min_time,max(g1,g2))
        return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,N,t)
            l.pop()
            
dfs([],N,t)
print(min_time)