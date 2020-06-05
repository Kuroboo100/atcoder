S=input()

l=[]
i=0
if len(S)%2==0:
    for n in range(len(S)//2):
        l.append(S[n])
    for n in range(len(S)//2,len(S)):
        a=l.pop()
        if S[n]!=a:
            i+=1
    print(i)

else:
    for n in range(len(S)//2):
        l.append(S[n])
    for n in range(len(S)//2+1,len(S)):
        a=l.pop()
        if S[n]!=a:
            i+=1
    print(i)
