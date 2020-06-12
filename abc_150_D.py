def cal_minX(A,N,M):
    """
    hit A内の数全てでXが割り切れ、かつ商が奇数だったらTrue
    """
    modA=list(map(lambda x:x%2,A))
    max_A=max(A)
    #A内に偶奇が混在する場合は解が存在しない
    if len(set(modA))==2:
        no_ans=True
        minX=0
    else:
        fin=False
        no_ans=False
        i=0
        while fin==False:
            coef=2*i+1
            if max_A*coef>M:
                fin=True
                no_ans=True
            else:
                hit=True
                for n in range(N):
                    if max_A*coef%A[n]==0:
                        if (max_A*coef//A[n])%2==1:
                            pass
                        else:
                            hit=False
                            break
                    else:
                        hit=False
                        break

                if hit==False:
                    i+=1
                else:
                    fin=True
        minX=max_A*coef
    return no_ans,minX

def main():
    #input
    N,M=map(int,input().strip().split())
    A=list(map(int,input().strip().split()))
    A=list(map(lambda x:x//2,A))
    
    #題意を満たす最小のXを求める。
    no_ans,minX=cal_minX(A,N,M)
    #1-Mの中にminXの奇数倍数がいくつあるか調べる
    if minX>M or no_ans:
        return 0
    else:
        if M//minX%2==1:
            return M//minX//2+1
        else:
            return M//minX//2
if __name__=="__main__":
    print(main())
    

