N=int(input())
A=list(map(int,input().strip().split()))

#降った雨の総量
rain=sum(A)
#山Nに降った雨の量
r_N=rain
for  n in range(1,N):
    if n%2==1:
        r_N-=2*A[n-1]

ans=[]
tmp=r_N
for n in range(N):
    tmp=A[n-1]*2-tmp
    ans.append(tmp)

print(" ".join(list(map(str,ans))))


