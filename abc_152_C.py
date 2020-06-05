N=int(input())
P=list(map(int,input().strip().split()))

minlist=[]
for n in range(N):
    if n==0:
        minlist.append(1)
    elif P[n]==min(P[:n+1]):
        minlist.append(1)
    else:
        pass
print(sum(minlist))