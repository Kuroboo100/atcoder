def conv(A,N):
    #A(座標iの電灯の強さリスト)からB(座標iを照らしている電灯数)への変換
    #累積和を使う
    B_=[0 for n in range(N)]
    for n in range(1,N+1):
        il_min=max(n-A[n-1],1)
        il_max=min(n+A[n-1],N)
        B_[il_min-1]+=1
        if il_max<=N-1:
            B_[il_max]-=1

    B=[0 for n in range(N)]
    B[0]=B_[0]
    for n in range(1,N):
        B[n]=B[n-1]+B_[n]
    return B

def main():
    #input
    N,K=map(int,input().strip().split())
    A=list(map(int,input().strip().split()))
    
    if K>45:
        return " ".join(map(str,[N for n in range(N)]))
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

    
