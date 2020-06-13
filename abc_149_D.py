def f(c):
    """
    入力に対する勝ち手を出力
    """
    if c=="r":
        return "p"
    elif c=="s":
        return "r"
    else:
        return "s"

def main():
    """
    まずは全て勝つ組み合わせを作って、合計ポイントを求める。
    iを0からN-Kまで変化させ、T(i)=T(k+i)となる時、
    T(k+i)をT(i)、T(i+2K)と異なる手に変更する。
    ※T(i)を変更すると、T(i)=T(i+k)=T(i+2K)=...=と連続した時に、
    全て変更されてスコアが最大にならない。
    T(k+i)は勝ちから"あいこまたは負け"に変化するので、合計ポイントから差っ引く。
    """

    #input
    N,K=map(int,input().strip().split())
    R,S,P=map(int,input().strip().split())
    T=list(input())
    
    win_T=list(map(lambda x:f(x),T))
    point={"r":R,"s":S,"p":P}
    score=sum([point[win_T[n]] for n in range(N)])
    for i in range(N-K):
        l=["r","s","p"]
        if win_T[i]==win_T[i+K]:
            score-=point[win_T[i+K]]
            l.remove(win_T[i])
            if i<=N-2*K-1 and win_T[i]!=win_T[i+2*K]:
                l.remove(win_T[i+2*K])
            win_T[i+K]=l[0]
    return score

if __name__=="__main__":
    print(main())