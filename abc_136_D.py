def binary_search3(A,x):
    if x<A[0]:
        OK=0
        NG=0
    elif x>A[len(A)-1]:
        OK=len(A)-1
        NG=len(A)-1
    else:
        OK=0
        NG=len(A)
        DIV=(OK+NG)//2
        while OK+1<NG:
            if x>=A[DIV]:
                OK=DIV
            else:
                NG=DIV
            DIV=(OK+NG)//2
    return OK,NG

def main():
    #input
    S=list(input())
    r=[]
    l=[]
    for n in range(len(S)):
        if S[n]=="R":
            r.append(n)
        else:
            l.append(n)
    num=[1 for _ in range(len(S))]
    #R>>>L
    for n in range(len(r)):
        tmp=l[binary_search3(l,r[n])[1]]
        if (tmp-r[n])%2==0:
            num[tmp]+=1
        else:
            num[tmp-1]+=1
        num[r[n]]-=1
    #R<<<L
    for n in range(len(l)):
        tmp=r[binary_search3(r,l[n])[0]]
        if (tmp-l[n])%2==0:
            num[tmp]+=1
        else:
            num[tmp+1]+=1
        num[l[n]]-=1

    return " ".join(map(str,num))

if __name__=="__main__":
    print(main())

    