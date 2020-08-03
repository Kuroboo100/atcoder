def main():#検算回路
    N=int(input())
    #各交通機関の移動人数
    t=[int(input()) for _ in range(5)]
    #初期値　所要時間、各都市の人数
    m=0
    p=[N,0,0,0,0,0]
    tran=[0 for _ in range(len(t))]
    while p[5]<N:
        #移動人数の算出
        for n in range(5):
            tran[n]=min(t[n],p[n])
        #移動(発送)
        for n in range(5):
            p[n]=max(0,p[n]-tran[n])
        #移動(受け入れ)
        for n in range(1,6):
            p[n]=p[n]+tran[n-1]
        m+=1
        print(p)
    print(m)

def main2():
    N=int(input())
    #各交通機関の移動人数
    t=[int(input()) for _ in range(5)]
    MIN=min(t)
    if N%MIN==0:
        m=N//MIN+4
    else:
        m=N//MIN+1+4
    print(m)

if __name__=="__main__":
    main2()