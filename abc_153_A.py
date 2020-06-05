HA=list(map(int,input().strip().split()))
H=HA[0]
A=HA[1]

if H%A==0:
    print(H//A)
else:
    print(H//A+1)