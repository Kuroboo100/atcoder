S=list(input())
N=len(S)-1

all_sum=0
def dfs(l,N,S):
    X=[[] for n in range(N+1)]
    X[0]=[S[0]]
    cnt=0
    temp=0
    if len(l)==N:
        global all_sum
        for n in range(N):
            if l[n]==0:
                X[cnt].append(S[n+1])
            else:
                cnt+=1
                X[cnt].append(S[n+1])
        for i in range(N+1):
            if X[i]!=[]:
                temp+=int("".join(X[i]))
        all_sum+=temp         
        return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,N,S)
            l.pop()
dfs([],N,S)
print(all_sum)