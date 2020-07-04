N,K=map(int,input().strip().split())
a=list(map(int,input().strip().split()))

ans=0
s=0
i=0
while s<K and i<=N-1:
    s+=a[i]
    if s<K:
        i+=1
ans+=N-i
print("i "+str(i))
print(ans)

for n in range(N):
    s-=a[n]
    if s>=K:
        ans+=N-i
    else:
        while s<K and i<=N-2:
            i+=1
            s+=a[i]
        if s>=K:
            ans+=N-i
    print("n "+str(n)+" i "+str(i))
    print(ans)

print(ans)
