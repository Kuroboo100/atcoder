def q1(n,point,ac,N,M):
    score=0
    for m in range(M):
        if ac[n-1][m-1]==1:
            score+=point[m-1]
    print(score)

def q2(n,m,point,ac):
    ac[n-1][m-1]=1
    point[m-1]-=1
    return

def main():
    #入力
    N,M,Q=map(int,input().strip().split())
    #各問題のポイント Nで初期化
    point=[N for m in range(M)]
    #各参加者の正答状況 0で初期化、正解で1
    ac=[[0 for m in range(M)] for n in range(N)]
    for _ in range(Q):
        #クエリ入力
        s=list(map(int,input().strip().split()))
        if s[0]==1:
            q1(s[1],point,ac,N,M)
        else:
            q2(s[1],s[2],point,ac)

if __name__=="__main__":
    main()

