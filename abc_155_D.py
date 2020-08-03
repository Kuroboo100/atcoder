def mul_minus(m,p,k):
    """
    m,p=minus またはplus
    順番はminus>>plusの順で与える
    出力はl,sの積の組み合わせでk番目に小さい数
    """
    p.sort(reverse=True)
    m_tmp=0
    p_tmp=0
    i=0
    mul=[m[0]*p[0]]
    while i<k:
        if p_tmp+1<len(p):
            can_1=m[m_tmp]*p[p_tmp+1]
        if m_tmp+1<len(m):
            can_2=m[m_tmp+1]*p[p_tmp]

        if can_1>=can_2:
            m_tmp=m_tmp+1
        else:
            p_tmp=p_tmp+1
        mul.append(m[m_tmp]*p[p_tmp])
        i+=1
    return m[m_tmp]*p[p_tmp]

def mul_plus(m,p,k):
    """
    m,p=minus またはplus
    順番はminus>>plusの順で与える
    出力はl,sの積の組み合わせでk番目に小さい数
    """
    m.sort(reversed=True)
    tmp=[0,1,0,1]
    sm_tmp=tmp[0]
    lm_tmp=tmp[1]
    sp_tmp=tmp[2]
    lp_tmp=tmp[3]
    i=0
    can=[0,0,0,0]
    mul=[]
    while i<k:
        if sm_tmp+1!=lm_tmp and sm_tmp+1<len(m):
            can[0]=m[sm_tmp+1]*m[lm_tmp]
        if lm_tmp+1<len(m):
            can[1]=m[sm_tmp]*m[lm_tmp+1]
        if sp_tmp+1!=lp_tmp and sp_tmp+1<len(p):
            can[2]=p[sp_tmp+1]*p[lp_tmp]
        if lp_tmp+1<len(p):    
            can[3]=p[sp_tmp]*p[lp_tmp+1]

        if can_1>=can_2:
            lm_tmp+=1
        else:
            sm_tmp+=1
        j=can.index(min(can))
        tmp[j]+=1
        i+=1
        mul.append(min(can))
    return min(can)

def main():
    N,K=map(int,input().strip().split())
    A=list(map(int,input().strip().split()))

    A.sort()
    minus=[]
    zero=[]
    plus=[]
    for n in range(N):
        if A[n]<0:
            minus.append(A[n])
        elif A[n]==0:
            zero.apppend(A[n])
        else:
            plus.append(A[n])

    num_minus=len(minus)*len(plus)
    num_zero=len(zero)*len(minus)+len(zero)*len(plus)
    num_plus=len(plus)*(len(plus)-1)+len(minus)*(len(minus)-1)

    if K<=num_minus:
        return  mul_minus(minus,plus,K)
    elif num_minus<K<=num_minus+num_zero:
        return 0
    else:
        k=K-num_minus-num_zero
        return  mul_plus(minus,plus,k)

if __name__=="__main__":
    print(main())
