#true or false
def binary_search(A,n):
    find=False
    start=0
    end=len(A)
    if A[0]==n:
        find=True
    else:
        while find==False and start<end-1:
            middle=(start+end)//2
            if n>A[middle]:
                start=middle
            elif n<A[middle]:
                end=middle
            else:
                find=True
    return find

#value
def binary_search2(A,n):
    find=False
    start=0
    end=len(A)
    if A[0]==n:
        find=True
    else:
        while find==False and start<end-1:
            middle=(start+end)//2
            if n>A[middle]:
                start=middle
            elif n<A[middle]:
                end=middle
            else:
                find=True
    if find==True:
        value=A.index(n)
    else:
        value=start
    return value

#OK NG method
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

N=100
A=[n**2+100 for n in range(N)]
x=10000

print(A)
print(binary_search3(A,x))
print(A[binary_search3(A,x)[0]],A[binary_search3(A,x)[1]])


            

        