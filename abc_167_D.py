N,K=map(int,input().strip().split())
A=list(map(int,input().strip().split()))

l=[1]
x=1
cnt=[0 for n in range(N)]
cnt[0]=1
for n in range(N):
    y=A[x-1]
    l.append(y)
    cnt[y-1]+=1
    x=y
    if cnt[y-1]==2:
        value=y
        temp=n
        break

for m in range(len(l)):
    if l[m]==value:
        bias=m
        mul=temp-bias+1
        break
    
if bias>K:
    print(l[K])
else:
    print(l[bias+(K-bias)%mul])