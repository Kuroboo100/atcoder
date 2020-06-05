S=list(input())
T=list(input())

ans=True
if len(T)-len(S)==1:
    for n in range(len(S)):
        if S[n]!=T[n]:
            ans=False
else:
    ans=False

if ans==True:
    print("Yes")
else:
    print("No")
    
    