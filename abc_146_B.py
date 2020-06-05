l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=int(input())
S=list(input())
c=N%26

Sdash=[]
for e in S:
    if l.index(e)+c>=26:
        Sdash.append(l[c-(26-l.index(e))])
    else:
        Sdash.append(l[l.index(e)+c])
print("".join(Sdash))


