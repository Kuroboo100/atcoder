H=int(input())

def dfs(h):
    if h==1:
        return 1
    else:
        if h%2==0:
            return dfs(h//2)*2+1
        else:
            return dfs((h-1)//2)*2+1

print(dfs(H))