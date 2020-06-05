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
    OK=A[0]-1
    NG=len(A)
    DIV=(OK+NG)//2
    while OK+1<NG:
        if x>=A[DIV]:
            OK=DIV
        else:
            NG=DIV
        DIV=(OK+NG)//2
    return OK 

N=10
A=[2*n for n in range(N)]
x=7

print(A)
print(binary_search3(A,x))
print(A[binary_search3(A,x)])


            

        