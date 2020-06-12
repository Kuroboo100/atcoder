from collections import deque

def bfs(S,s,H,W):
    dx=[1,0,0,-1]
    dy=[0,1,-1,0]
    d=deque([s])
    visited=[[-1 for _ in range(W)] for _ in range(H)]
    visited[s[0]][s[1]]=0
    max_time_=0
    while d:
        root=d.popleft()
        prev=visited[root[0]][root[1]]
        for n in range(len(dx)):
            n_x=root[0]+dx[n]
            n_y=root[1]+dy[n]
            if (0<=n_x<=H-1) and (0<=n_y<=W-1):
                if S[n_x][n_y]=="." and visited[n_x][n_y]==-1:
                    d.append((n_x,n_y))
                    visited[n_x][n_y]=prev+1
                    max_time_=max(max_time_,prev+1)
    return max_time_

def main():
    #スタート地点を固定し、全てのマスへの移動回数を全探索し、最大移動回数を求める。
    #スタート地点を全探索し、最大移動回数内の最大値を答えとして出力する。
    #input
    H,W=map(int,input().strip().split())
    S=[list(input()) for _ in range(H)]
    
    #スタート地点を固定し、sg_listに格納。
    #スタート地点〜全ての"."を探索し、最も遠い点をsg_listに格納する。
    #最も遠い点までの移動回数をturns_listに格納する。
    sg_list=[]
    max_time=0
    for w in range(W):
        for h in range(H):
            if S[h][w]=="." and (h,w) not in sg_list:
                start=(h,w)
                sg_list.append((h,w))
                max_time=max(max_time,bfs(S,start,H,W))
    return max_time

if __name__=="__main__":
    print(main())

