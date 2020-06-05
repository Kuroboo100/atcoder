K=int(input())
A,B=map(int,input().strip().split())

OK=False
for n in range(A,B+1):
    if n%K==0:
        OK=True
        break

if OK:
    print("OK")
else:
    print("NG")
        