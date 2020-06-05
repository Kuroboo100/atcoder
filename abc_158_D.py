S=input()
Q=int(input())

states=1
front=[]
back=[]
for n in range(Q):
    query=input()
    if query=="1":
        states*=-1
    else:
        N,F,C=query.strip().split()
        if int(F)==1:
            if states==1:
                front.append(C)
            else:
                back.append(C)
        else:
            if states==1:
                back.append(C)
            else:
                front.append(C)

if states==1:
    print("".join(front)[::-1]+S+"".join(back))
else:
    print("".join(back)[::-1]+S[::-1]+"".join(front))
            