def q1(C,x,a):
    if C[x-1]<a:
        pass
    elif C[x-1]>=a:
        C[x-1]-=a
    return C

def q2(C,a,N):
    less=False
    for n in range(N//2):
        if C[2*n]<a:
            less=True
            break
    if less==False:
        for n in range(N//2):
            C[2*n]-=a
    else:
        pass
    return C

def q3(C,a,N):
    less=False
    for n in range(N):
        if C[n]<a:
            less=True
            break
    if less==False:
        C=list(map(lambda x:x-a,C))
    else:
        pass
    return C

def main():
    N=int(input())
    C=list(map(int,input().strip().split()))
    Q=int(input())
    S=[list(map(int,input().strip().split())) for n in range(Q)]
    C_ini_number=sum(C)
    
    for element in S:
        if element[0]==1:
            C=q1(C,element[1],element[2])
        elif element[0]==2:
            C=q2(C,element[1],N)
        elif element[0]==3:
            C=q3(C,element[1],N)
    return C_ini_number-sum(C)

print(main())
