#5/15 AC
def dfs(xy,n,m,N,M):
    dx=[-1,0,0,1]
    dy=[0,1,-1,0]
    if xy[n][m]=="o":
        stack=[[n,m]]
        while stack!=[]:
            exe=stack.pop()
            for i in range(len(dx)):
                temp=[exe[0]+dx[i],exe[1]+dy[i]]
                if N-1>=temp[0]>=0 and M-1>=temp[1]>=0:
                    if xy[temp[0]][temp[1]]=="o" and temp not in stack:
                        stack.append(temp)
                        xy[temp[0]][temp[1]]="x"
    able=True
    for n in range(N):
        for m in range(M):
            if xy[n][m]=="o":
                able=False
    return able

def full_search(N,M,xy):
    t=tuple(xy[n] for n in range(len(xy)))
    new_xy=[]
    for n in range(N):
        for m in range(M):
            xy_l=[list(t[n]) for n in range(len(t))]
            if xy_l[n][m]=="x":
                xy_l[n][m]="o"
                new_xy.append(xy_l)
    return new_xy

def main():
    N=10
    M=10
    xy=[]
    for n in range(N):
        xy.append(list(input().strip()))
        
    ans=False
    S=full_search(N,M,xy)
    for e in S:
        t=tuple(e[n] for n in range(len(e)))
        for n in range(N):
            for m in range(M):
                l=[list(t[i]) for i in range(len(t))]
                if dfs(l,n,m,N,M):
                    ans=True
                    break
        if ans==True:
            break
    if ans==True:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
        
                
        