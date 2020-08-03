L,R=map(int,input().strip().split())

if R-L>=2019:
    print(0)
else:
    minimum=2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            minimum=min((i*j)%2019,minimum)
    print(minimum)
