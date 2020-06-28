S=list(input())
T=list(input())
cnt=0
for n in range(len(T)):
    if S[n]!=T[n]:
        cnt+=1
print(cnt)

