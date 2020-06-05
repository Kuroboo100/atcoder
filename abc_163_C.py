N=int(input())
A=list(map(int,input().strip().split()))

num=[0 for n in range(N)]
for i in range(N-1):
    num[A[i]-1]+=1

for n in range(len(num)):
    print(num[n])
