N=list(map(int,list(input())))

for n in range(2**3):
    sum_N=N[0]
    l=[]
    for i in range(3):
        if (n>>i)&1==1: #convert from decimal to binary and shift right
            sum_N+=N[i+1]
            l.append("+")
        else:
            sum_N-=N[i+1]s
            l.append("-")
    if sum_N==7:
        break
print("{}{}{}{}{}{}{}".format(N[0],l[0],N[1],l[1],N[2],l[2],N[3])+"=7")



