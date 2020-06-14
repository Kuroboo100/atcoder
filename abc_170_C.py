X,N=map(int,input().strip().split())
if N>=1:
    P=list(map(int,input().strip().split()))
else:
    P=[]

Y=X
while X in P and Y in P:
        X+=1
        Y-=1

if  Y not in P:
    print(Y)
else:
    print(X)

        
