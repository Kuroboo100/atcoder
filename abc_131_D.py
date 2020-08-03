N=int(input())
A=[]
B=[]
for n in range(N):
    a,b=map(int,input().strip().split())
    A.append(a)
    B.append((b,n))

B=sorted(B)

sumA=0
fin=True
for n in range(N):
    tmp=B[n][1]
    sumA+=A[tmp]
    if sumA>B[n][0]:
        fin=False
        break

if fin==True:
    print("Yes")
else:
    print("No")
