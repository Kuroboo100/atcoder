"""
"正の整数 N が与えられます。
N 以下の正の整数の組 (A,B)

であって、次の条件を満たすものの個数を求めてください。

    A,B

を先頭に 0 のつかない 10 進数表記で表したときに、 A の末尾の桁が B の先頭の桁に等しく、 A の先頭の桁が B

    の末尾の桁に等しい

制約

    1≤N≤2×105

    入力はすべて整数である。

入力

入力は以下の形式で標準入力から与えられる。

N
"""


# =============================================================================
# N=int(input())
# Nlist=str(N)
# 
# num=0
# 
# for n in range(N):
#     digit=len(Nlist)
#     l=list(str(n))
#     a=int(l[0])
#     b=int(l[-1])   
#     
#     if b<int(Nlist[0]):
#         while digit-2>=0:
#             num+=10**(digit-2)
#             digit-=1
#     elif b>int(Nlist[0]):
#         while digit-3>=0:
#             num+=10**(digit-2)
#             digit-=1
#     else:
#         while digit-3>=0:
#             num+=10**(digit-2)
#             digit-=1
#         if digit<3:
#             pass
#         else:
#             if a<=int(Nlist[-1]):
#                 num+=int("".join(Nlist[1:-1]))
#             else:
#                 num+=int("".join(Nlist[1:-1]))-1
# print(num)
# =============================================================================

N=int(input())
A=[[0 for n in range(9)] for n in range(9)]

for n in range(N+1):
    head=int(str(n)[0])
    tail=n%10
    if head!=0 and tail!=0:
        A[head-1][tail-1]+=1

count=0

for i in range(9):
    for j in range(9):
        count+=A[i][j]*A[j][i]

print(count)
    
        
        