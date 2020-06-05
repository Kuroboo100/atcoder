N=int(input())
S=input()
R=[]
G=[]
B=[]

for n in range(N):
    if S[n]=="R":
        R.append(n)
    elif S[n]=="G":
        G.append(n)
    else:
        B.append(n)

ANS=len(R)*len(G)*len(B)

for i in range(N-2):
    for j in range(i+1,N-1):
        k=2*j-i
        if k<N and S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
            ANS-=1


print(ANS)


    