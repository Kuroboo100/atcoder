"""
ボールが N 個あり、 i 番目のボールには整数 Ai が書かれています。
k=1,2,...,N
に対して以下の問題を解いて、答えをそれぞれ出力してください。
k番目のボールを除いた N−1 個のボールから、書かれている整数が等しいような異なる 2
つのボールを選び出す方法の数を求めてください。選ぶ順序は考慮しません。

制約
3≤N≤2×105
1≤Ai≤N
入力はすべて整数である。

入力
入力は以下の形式で標準入力から与えられる。
N
A1
A2
...
AN

出力
k=1,2,...,N
に対する答えを順番に一行ずつ出力せよ。
"""

N=int(input())
A=list(map(int,input().strip().split()))

l=[0 for n in range(N)]

for e in A:
    l[e-1]+=1

count=0
for n in range(N):
    if l[n]>=2:
        count+=l[n]*(l[n]-1)//2
            
for n in range(N):
    print(count-l[A[n]-1]+1)

