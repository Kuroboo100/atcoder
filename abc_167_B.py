A,B,C,K=map(int,input().strip().split())

if K<=A:
    print(K)
elif A<K<=A+B:
    print(A)
else:
    print(A-(K-(A+B)))