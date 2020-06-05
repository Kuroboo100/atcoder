HN=list(map(int,input().strip().split()))
H=HN[0]
N=HN[1]
A=list(map(int,input().strip().split()))

if sum(A)>=H:
    print("Yes")
else:
    print("No")