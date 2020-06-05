N=int(input())
A=[[0 for m in range(n)]+list(map(int,input().strip().split())) for n in range(N-1)]

def dec_to_three(n,N):
    temp=n
    glist=[]
    for i in range(N):
        if temp<3**(N-i-1):
            glist.append(0)
            pass
        else:
            if temp>=2*3**(N-i-1):
                glist.append(2)
                temp-=2*3**(N-i-1)
            elif temp>=3**(N-i-1):
                glist.append(1)
                temp-=3**(N-i-1)
    return glist
 
def grouping(dec,N):
    label=dec_to_three(dec,N)
    group_0=[]
    group_1=[]
    group_2=[]
    for n in range(N):
        if label[n]==0:
            group_0.append(n+1)
        if label[n]==1:
            group_1.append(n+1)
        if label[n]==2:
            group_2.append(n+1)
    return group_0,group_1,group_2

def score_calcurate(group,A):
    #group score
    score=0
    for n in range(len(group)):
        for m in range(n+1,len(group)):
            score+=A[group[n]-1][group[m]-2]
    return score

def max_score(A,N):
    max_score=-100000000
    max_group=[]
    for n in range(3**N):
        group=grouping(n,N)
        total_score=0
        for i in range(3):
            total_score+=score_calcurate(group[i],A)
        if max_score<total_score:
            max_group=group
            max_score=total_score

    return max_score,max_group

print(max_score(A,N)[0])
#print(max_score(A,N)[1])
