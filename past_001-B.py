N=int(input())
A=[int(input()) for n in range(N)]
result=[0 for n in range(N-1)]

for n in range(N-1):
    if A[n+1]>A[n]:
        judge="up"
        sub=str(A[n+1]-A[n])
    elif A[n+1]==A[n]:
        judge="stay"
        sub=""
    else:
        judge="down"
        sub=str(A[n]-A[n+1])
    temp=[judge,sub]
    element=" ".join(temp)
    result[n]=element

print(*result,sep="\n")
