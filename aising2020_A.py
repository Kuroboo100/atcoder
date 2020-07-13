L,R,d=map(int,input().strip().split())
cnt=0
for n in range(L,R+1):
    if n%d==0:
        cnt+=1
print(cnt)