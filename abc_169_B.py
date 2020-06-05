N=int(input())
A=list(map(int,input().strip().split()))

INF=1000000000000000000
if 0 in A:
    print(0)
else:
    ans=1
    for n in range(N):
        ans*=A[n]
        if ans>INF:
            break

    if ans>INF:
        print(-1)
    else:
        print(ans)
