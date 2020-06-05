N,X,Y=map(int,input().strip().split())

distance=[0 for n in range(N-1)]

for i in range(1,N):
    for j in range(i+1,N+1):
        k=min(abs(i-j),abs(X-i)+1+abs(Y-j),abs(X-j)+1+abs(Y-i))
        if k!=0:
            distance[k-1]+=1

for e in distance:
    print(e)
        
