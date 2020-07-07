from collections import deque
#input
N,M=map(int,input().strip().split())
A=list(map(int,input().strip().split()))

#M回全て、その時点で一番高価な商品に割引を
#適用した時、支払金額が最小となる。

#安い順にソート
A.sort()

#割引券を一回でも使った商品を格納
dp=deque([])
#割引未適用品(A)と、適用済み品(dp)の最高値を比較し、大きい方に割引を適用
for m in range(M):
    if len(dp)==0:
        tmp=A.pop()
    elif len(A)==0:
        tmp=dp.popleft()
    else:
        if A[-1]>=dp[0]:
            tmp=A.pop()
        else:
            tmp=dp.popleft()
    dp.append(tmp//2)
print(sum(A)+sum(dp))


    