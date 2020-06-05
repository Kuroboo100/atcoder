import math
N=int(input())
n=int(math.sqrt(N))
MAX=1
for i in range(1,n+1):
    if N%i==0:
        MAX=i

print(MAX+N//MAX-2)

