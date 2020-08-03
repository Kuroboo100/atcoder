import math
N,D=map(int,input().strip().split())
cnt=0
for n in range(N):
    X,Y=map(int,input().strip().split())
    if math.sqrt(X**2+Y**2)<=D:
        cnt+=1
print(cnt)