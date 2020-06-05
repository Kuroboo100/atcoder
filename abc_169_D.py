#ボツ。会社のPCでAC。コードは提出結果参照
import math
N=int(input())

def prime(x):
    prime=True
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            prime=False
            break
    return prime

NN=[]
goon=True
divider=[0 for n in range(int(math.sqrt(N))+1)]
while goon==True:
    NN.append(N)
    rootN=int(math.sqrt(N))+1
    for i in range(2,rootN):
        if N%i==0 and prime(i)==True:
            divider[i]+=1
            N//=i
            break
        if prime(N):
            goon=False

ans=0
for n in range(len(divider)):
    ans+=divider[n]*(divider[n]-1)//2

print(ans)

