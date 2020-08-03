N=int(input())
H=list(map(int,input().strip().split()))

MAX=H[0]

for n in range(N):
    if MAX-H[n]>=2:
        print("No")
        break
    else:
        MAX=max(MAX,H[n])
else:
    print("Yes")
