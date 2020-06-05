S=list(map(int,input()))
sum_S=0
l=[0]
for n in range(2**len(S)):
    for i in range(len(S)):
        if (n>>i)&1==1:
            l.append(i)
    l.append(len(S))

for m in range(len(l)):
    sum_S+=int("".join(map(str,S[l[m]:l[m+1]])))

print(sum_S)

#bit全探索