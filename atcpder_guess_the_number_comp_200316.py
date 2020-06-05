def guess(N,M,S,C,guess_num):
    no_num=False
    if len(guess_num)!=1:
        guess_num[0]=1
    else:
        pass

    num_input=[0 for n in range(N)]
    for m in range(M):
        if num_input[S[m]-1]==0 or guess_num[S[m]-1]==C[m]:
            guess_num[S[m]-1]=C[m]
            num_input[S[m]-1]=1
        else:
            no_num=True
            break
    
    if no_num==True or (len(guess_num)!=1 and guess_num[0]==0):
        return -1
    else:
        return int("".join(map(str,guess_num)))

def main():
    #initialize
    NM=[]
    SC=[]
    #input
    NM=list(map(int,input().strip().split()))
    N=NM[0]
    M=NM[1]
    for n in range(M):
        SC.append(list(map(int,input().strip().split())))
    S=[SC[i][0] for i in range(M)]
    C=[SC[j][1] for j in range(M)]

    guess_num=[0 for n in range(N)]
    
    print(guess(N,M,S,C,guess_num))

main()
            
