A,B,C,D=map(int,input().strip().split())

fin=False
while fin==False:
    C-=B
    if C<=0:
        fin=True
        win="t"
    else:
        A-=D
        if A<=0:
            fin=True
            win="a"
        else:
            pass

if win=="t":
    print("Yes")
else:
    print("No")