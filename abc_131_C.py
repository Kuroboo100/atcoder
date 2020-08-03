A,B,C,D=map(int,input().strip().split())

"""
Cで割れる数とDで割れる数を総数(B-A+1)から引く。
CとDの公倍数を二重に引いているので,
CとDの最小公倍数で割れる数を足し戻す。

A以上B以下のうち、Xで割れる数の個数は以下で表される。
B//X-A//X　※(B-A)//Xではない
AがXで割れる数だった場合、上記だとAも引いてしまうことになるため、
B//X-A//X+1とすることに注意。
"""

if A%C==0:
    c=B//C-A//C+1
else:
    c=B//C-A//C

if A%D==0:
    d=B//D-A//D+1
else:
    d=B//D-A//D

def gcd(C,D):
    a=min([C,D])
    b=max([C,D])
    tmp=a
    a=b%a
    b=tmp
    if a==0:
        return tmp
    else:
        return gcd(a,b)

CD=C*D//gcd(C,D)
if A%CD==0:
    cd=B//CD-A//CD+1
else:
    cd=B//CD-A//CD

print((B-A+1-c-d+cd))