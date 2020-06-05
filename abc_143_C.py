N=int(input())
S=input()

l=list(S)
ans=[l[0]]
for n in range(1,N):
    if l[n]!=l[n-1]:
        ans.append(l[n])

print(len(ans))
