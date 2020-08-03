N=int(input())
B=list(map(int,input().strip().split()))

ans=B[0]+B[N-2]
for n in range(N-2):
    ans+=min(B[n],B[n+1])
print(ans)