def conv(A,N):
    #A(座標iの電灯の強さリスト)からB(座標iを照らしている電灯数)への変換
    B=[0 for n in range(N)]
    for n in range(1,N+1):
        il_min=max(int(n-A[n-1]-0.5)+1,0)
        il_max=min(int(n+A[n-1]+0.5),N)
        B_=[B[i]+1 for i in range(N) if il_min<=i<=il_max]
    return B_

def main():
    #input
    N,K=map(int,input().strip().split())
    A=list(map(int,input().strip().split()))

    if K>30:
        A=[N for n in range(N)]
        A[-1]=2*N
    else:
        for k in range(K):
            B=conv(A,N)
            if A==B:
                break
            else:
                A=B
    return " ".join(list(map(str,A)))

if __name__=="__main__":
    print(main())
    
