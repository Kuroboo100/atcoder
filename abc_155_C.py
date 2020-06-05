N=int(input())
S=[input() for n in range(N)]

S.sort()

l=[]
c=[]
prev=""
cnt=0
for e in S:
    if e==prev:
        cnt+=1
    else:
        c.append(cnt)
        cnt=0
        l.append(e)
        prev=e

print(S)
print(l)
print(c)

        
