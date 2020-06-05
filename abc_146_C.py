A,B,X=map(int,input().strip().split())

for i in range(9):
    N=X//A-((B*i)//A+1)
    if len(list(str(N)))==i:
        ans=N
        break
    else:
        ans=0

if N>1000000000:
    print(1000000000)
elif N<=0:
    print(0)
else:
    print(ans)

# N=0
# OVER=False
# while OVER==False:
#     S=len(list(str(N)))
#     cost=A*N+B*S
#     if cost>X:
#         OVER=True
#     else:
#         N+=1

# if N==0:
#     print(N)
# elif N>1000000000:
#     print(1000000000)
# else:
#     print(N-1)
