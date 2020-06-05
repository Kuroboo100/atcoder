N=int(input())
L=list(map(int,input().strip().split()))
sort_L=sorted(L)

def binary_search3(A,x):
    OK=-1
    NG=len(A)
    DIV=(OK+NG)//2
    while OK+1<NG:
        if x>=A[DIV]:
            OK=DIV
        else:
            NG=DIV
        DIV=(OK+NG)//2
    return OK 

count=0
for a in range(len(L)):
    for b in range(a+1,len(L)):
        MAX=binary_search3(sort_L,L[a]+L[b]-1)
        MIN=binary_search3(sort_L,max(L[a],L[b]))
        print(L[a],L[b],MIN,MAX)
        count+=max(0,MAX-MIN)

print(count)
        


