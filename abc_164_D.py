#TLE
"""
1 から 9 までの数字のみからなる文字列 S

が与えられます。

次のような条件を満たす整数の組 (i,j)
(1≤i≤j≤|S|

) の総数を求めてください。

条件: S
の i 文字目から j 文字目までを 10 進法の整数としてみると、この整数は 2019

の倍数である。
制約

    1≤|S|≤200000

S

    は 1 から 9 までの数字のみからなる文字列

入力

入力は以下の形式で標準入力から与えられる。

S


"""

S=list(input())

l=[0 for n in range(2019)]

for n in range(4,len(S)+1):
    p=S[len(S)-n:len(S)]
    x=int("".join(p))
    m=x%2019
    l[m]+=1

num=0
for n in range(len(l)):
    if n==0:
        num+=l[n]+l[n]*(l[n]-1)//2
    else:
        num+=l[n]*(l[n]-1)//2

print(num)

















            