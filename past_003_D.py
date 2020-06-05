N=int(input())
s=[list(input()) for _ in range(5)]

num=[]
for n in range(N):
    cnt=0
    for i in range(4):
        for j in range(5):
            if s[j][4*n+i]=="#":
                cnt+=1
    if cnt==7:
        num.append(7)
    elif cnt==8:
        num.append(1)
    elif cnt==9:
        num.append(4)
    elif cnt==11:
        if s[1][4*n+3]=="#" and s[3][4*n+1]=="#":
            num.append(2)
        elif s[1][4*n+3]=="#" and s[3][4*n+3]=="#":
            num.append(3)
        else:
            num.append(5)
    elif cnt==12:
        if s[3][4*n+1]=="#" and s[1][4*n+3]=="#":
            num.append(0)
        elif s[3][4*n+1]=="#":
            num.append(6)
        else:
            num.append(9)
    else:
        num.append(8)

print(''.join(map(str,num)))

    
    