#5/16 WA
def dfs(x,uv,M):
    #print("hell0") #---------------------------------------------------
    """
    dfs of tree structure from start point(x)
    if the stacked point has already visited,
    dfs judge the tree structure as closed loop,return false.
    """
    open_loop=True
    stack=[x]
    visited=[]
    while stack:
        #print("stack",stack) #---------------------------------------------------
        exe=stack.pop()
        visited.append(exe)
        for n in range(M):
            if exe==uv[n][0] and uv[n][1] in visited:
                open_loop=False
            if exe==uv[n][0] and uv[n][1] not in visited:
                stack.append(uv[n][1])
    #print(open_loop,visited) #---------------------------------------------------
    return open_loop,visited

def main():
    #normal input value
    N,M=map(int,input().strip().split())
    uv=[list(map(int,input().strip().split())) for _ in range(M)]
    #initial value
    num=0
    done=[]
    for n in range(M):
        if uv[n][0] not in done:
            ans,visited=dfs(uv[n][0],uv,M)
            done+=visited
            if ans:
                num+=1
        #print("done",done) #---------------------------------------------------
    return num+(N-len(set(done)))
    
if __name__ == '__main__':
    print(main())
"""
11 11
1 2
1 3
2 4
3 5
4 6
5 7
6 8
7 9
8 10
9 11
10 11
"""
                    
                
    
