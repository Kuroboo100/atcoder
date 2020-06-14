X,Y=map(int,input().strip().split())

hit=False
for n in range(X+1):
    if 2*n+4*(X-n)==Y:
        hit=True
        break

if hit==True:
    print("Yes")
else:
    print("No")