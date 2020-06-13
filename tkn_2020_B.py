A,V=map(int,input().strip().split())
B,W=map(int,input().strip().split())
T=int(input())

if abs(B-A)<=(V-W)*T:
    print("YES")
else:
    print("NO")