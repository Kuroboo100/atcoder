N,A,B,C=map(int,input().strip().split())
l=[input() for n in range(N)]


def dfs():
    if A in l and B in l and C in l:
        return
    else:
        