N=int(input())

ans=False
for a in range(1,10):
    for b in range(1,10):
        if a*b==N:
            ans=True
        else:
            pass

if ans==True:
    print('Yes')
else:
    print("No")