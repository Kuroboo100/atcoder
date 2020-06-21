N,K=map(int,input().strip().split())
p=list(map(int,input().strip().split()))

p.sort()

ans=sum(p[:K])

print(ans)