N,K=map(int,input().strip().split())

num=0
for n in range(K,N+2):
    MIN=(n-1)*n//2
    MAX=(N+(N-n+1))*n//2
    num+=MAX-MIN+1

print(num%(10**9+7))

