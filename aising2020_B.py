N=int(input())
A=list(map(int,input().strip().split()))

cnt=0
for n in range(N):
    if (n+1)%2==1 and A[n]%2==1:
        cnt+=1
print(cnt)