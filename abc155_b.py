N=int(input())
A=list(map(int,input().strip().split()))
def border_judge(N,A):
    judge=True
    for n in range(len(A)):
        if A[n]%2==0:
            if A[n]%5==0 or A[n]%3==0:
                judge=True
            else:
                judge=False
                break
        else:
            pass

    if judge==True:
        return "APPROVED"
    elif judge==False:
        return "DENIED"

print(border_judge(N,A))

    
        