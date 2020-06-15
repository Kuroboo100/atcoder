def main():
    """
    要素数Amaxのbool配列lを生成し、初期値を全てTrueとする。
    Aを昇順にソートし、Aの要素を順に見て、要素の倍数インデックスを全てFalseにする、
    という操作を繰り返す。
    あるp=A[n]を見た時にl[p]==Trueの場合、A[n]は全てのA[j](j<n)で割り切れない。
    ※A[j]<A[n]の全ての倍数のいずれともA[n]が一致しないということは、A[n]はA[j]で割り切れないことを意味します。
    A[n]==A[n+1]の時にA[n]はA[n+1]で割り切れるが、この場合を除いてA[n]は任意のA[i]で
    割り切れないのでカウントを一つインクリメントする。
    Aの全ての要素について操作を完了した時のカウント値が答えとなる。
    """
    #input
    N=int(input())
    A=list(map(int,input().strip().split()))
    #昇順
    A.sort()
    #AmaxまでのTrue配列
    l=[True for _ in range(A[-1]+1)]
    
    cnt=0
    for n in range(N-1):
        if l[A[n]]==True:
            if A[n]==A[n+1]:
                l[A[n]]=False
            else:
                l[A[n]]=False
                cnt+=1
            i=1
            while i*A[n]<=A[-1]:
                l[A[n]*i]=False
                i+=1
    #最終項はn+1と比較できないので別で考える。
    if l[A[N-1]]==True:
        cnt+=1
        l[A[N-1]]=False
    return cnt

if __name__=="__main__":
    print(main())
    
