import math
K=int(input())

# def gcb(l):
#     gcb=0
#     for i in range(1,min(l)+1):
#         if sum([l[n]%i for n in range(len(l))])==0:
#             gcb=i
#     return gcb

s=0
#全て同じ
for a in range(K+1):
    s+=a
#二つ同じ：
for a in range(1,K+1):
    for b in range(a+1,K+1):
        s+=math.gcd(a,b)*6
#全て異なる
for a in range(1,K+1):
    for b in range(a+1,K+1):
        for c in range(b+1,K+1):
            s+=math.gcd(c,(math.gcd(a,b)))*6

print(s)
