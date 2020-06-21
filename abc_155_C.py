N=int(input())
S=[input() for n in range(N)]

S.sort()

l=[]
c=[]
prev=S[0]
cnt=0
for n in range(len(S)):
    if S[n]==prev:
        cnt+=1
    else:
        c.append(cnt)
        cnt=1
        l.append(prev)
        prev=S[n]
if cnt!=0:
    c.append(cnt)
    l.append(prev)

max_cnt=max(c)

max_str=[]
for n in range(len(c)):
    if c[n]==max_cnt:
       max_str.append(l[n])
max_str.sort()

for e in max_str:
    print(e) 


        
