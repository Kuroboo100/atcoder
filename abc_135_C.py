N=int(input())
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))
"""
添字が小さい方の街からどんどん倒していけば良い。
iとi+1を倒して、B[i+1]がまだ余っている場合に、
それをi+2のモンスター倒しに繰り越して利用する。
B[i]が余っている時、その余りをi+2以降のモンスター退治に繰り越さないよう注意
"""
remain=max(0,B[0]-A[0])
mons=min(A[0],B[0])
for n in range(1,N):
    mons+=min(remain+B[n],A[n])
    remain=max(0,B[n]-max(A[n]-remain,0))
mons+=min(remain,A[N])
print(mons)
    