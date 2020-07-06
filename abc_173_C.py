import numpy as np

H,W,K=map(int,input().strip().split())
c=[]
for n in range(H):
    c.append(list(input()))
for h in range(H):
    for w in range(W):
        if c[h][w]==".":
            c[h][w]=0
        else:
            c[h][w]=1
c=np.array(c)

cnt=0
def rec(l,H,W,K):
    global cnt
    if len(l)==H+W:
        t=c.copy()
        for i in range(len(l)):
            if i<=H-1:
                if l[i]==1:
                    t[i,:]=0
            else:
                if l[i]==1:
                    t[:,i-H]=0
        if np.sum(t)==K:
            cnt+=1
    else:
        for n in range(2):
            l.append(n)
            rec(l,H,W,K)
            l.pop()

rec([],H,W,K)
print(cnt)