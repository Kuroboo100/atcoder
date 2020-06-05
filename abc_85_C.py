NY=list(map(int,input().strip().split()))
N=NY[0]
Y=NY[1]

s=False
for a in range(N+1):
    for b in range(a,N+1):
        sumN=a*10000+(b-a)*5000+(N-b)*1000
        if sumN==Y:
            s=True
            x=a
            y=b-a
            z=N-b
    if s:
        break

if s==True:
    print("{} {} {}".format(x,y,z))
else:
    print("-1 -1 -1")