K,S=map(int,input().strip().split())

cnt=0
for a in range(K+1):
    for b in range(K+1):
        if S-K<=a+b<=S:
            cnt+=1
print(cnt)