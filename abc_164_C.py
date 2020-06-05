N=int(input())
S=[input() for n in range(N)]

S.sort()

i=1
prev=S[0]
for e in S:
    if prev!=e:
        i+=1
    prev=e


print(i)
    