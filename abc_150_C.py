def dfs(l,N):
    if len(l)==N:
        x.append(int("".join(map(str,l))))
        return
    else:
        for n in range(1,N+1):
            if n not in l:
                l.append(n)
                dfs(l,N)
                l.pop()

def main():
    N=int(input())
    P=list(input().strip().split())
    Q=list(input().strip().split())
    global x
    x=[]
    dfs([],N)
    x.sort()
    a=x.index(int("".join(P)))
    b=x.index(int("".join(Q)))
    return abs(a-b)

if __name__=="__main__":
    print(main())