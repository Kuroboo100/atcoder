from collections import deque
    
N=int(input())
A=list(map(int,input().strip().split()))
    
A.sort(reverse=True)
    
dp=deque([A[1]])
point=A[0]
cnt=0
for n in range(2,len(A)):
    if cnt==0:
        p=dp.popleft()
        cnt+=1
        dp.append(A[n])
        point+=p
    else:
        cnt=0
        dp.append(A[n])
        point+=p
    
print(point)




