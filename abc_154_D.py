def main():
    #input
    N,K=map(int,input().strip().split())
    P=list(map(int,input().strip().split()))
    
    #期待値行列
    E=list(map(lambda x:(x+1)*x//2/x,P))
    S=[0 for n in range(N-K+1)]
    for n in range(K):
        S[0]+=E[n]
    
    ans=S[0]
    for i in range(1,N-K+1):
        S[i]=S[i-1]-E[i-1]+E[i+K-1]
        ans=max(ans,S[i])
    print(ans)

if __name__=="__main__":
    main()