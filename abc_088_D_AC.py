#simple and high speed program
from collections import deque

def n_bfs(S,W,H):
    dx=(-1,0,1,0)
    dy=(0,1,0,-1)
    queue=deque([[0,0]])
    d=[[0]*W for _ in range(H)]
    d[0][0]=1
    while queue:
        x,y=queue.popleft()
        for n in range(4):
            nx,ny=x+dx[n],y+dy[n]
            if 0<=nx<=W-1 and 0<=ny<=H-1 and S[ny][nx]=="." and d[ny][nx]==0:
                queue.append([nx,ny])
                d[ny][nx]=d[y][x]+1
    return d[-1][-1]

def n_main():
    H,W=map(int,input().strip().split())
    S=[list(input()) for _ in range(H)]
    ans=n_bfs(S,W,H)
    num_dot=sum(s.count(".") for s in S)
    
    return num_dot-ans if ans!=0 else -1

if __name__=="__main__":
    print(n_main())
    
#---------------------------------------------------
#5/16 WA TLE
#5/17 AC
from collections import deque

def bfs(S,W,H):
    dx=(-1,0,1,0)
    dy=(0,1,0,-1)
    queue=deque([[0,0]])
    visited=[]
    goal=False
    cnt=deque([0])
    while queue and goal==False:
        exe=queue.popleft()
        C=cnt.popleft()
        for i in range(len(dx)):
            x=exe[0]+dx[i]
            y=exe[1]+dy[i]
            if [x,y]==[W-1,H-1]:
                goal=True
            elif 0<=x<=W-1 and 0<=y<=H-1 and S[y][x]==".":
                if [x,y] not in visited: #cause of high calculation cost
                    queue.append([x,y])
                    visited.append([x,y])
                    cnt.append(C+1) 
    return goal,C+1

def main():
    H,W=map(int,input().strip().split())
    S=[list(input()) for _ in range(H)]
    # number of dot
    num_sharp=0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                num_sharp+=1
    goal,num=bfs(S,W,H)
    if goal:
        return W*H-num_sharp-(num+1)
    else:
        return -1

# =============================================================================
# if __name__=="__main__":
#     print(main())
# =============================================================================
