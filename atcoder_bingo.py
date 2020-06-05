import random

A=[1,2,3,11,12,61,13,14,15]
#A=[random.randint(0,100) for j in range(9)]
N=10
b=[1,12,3,19,53,96,97,98,99,15]

def bingo_judge(A,b):
    bingo=0
    judge_list=[0,0,0,0,0,0,0,0,0]
    for number in b:
        for i in range(9):
            if number==A[i]:
                judge_list[i]=1
            else:
                pass
    #horizonal
    for i in range(3):
        if judge_list[3*i]*judge_list[3*i+1]*judge_list[3*i+2]==1:
            bingo=1
        else:
            pass
    #vertical
    for i in range(3):
        if judge_list[i]*judge_list[i+3]*judge_list[i+6]==1:
            bingo=1
        else:
            pass
    #diagonal
    if judge_list[0]*judge_list[4]*judge_list[8]==1:
        bingo=1
    if judge_list[2]*judge_list[4]*judge_list[6]==1:
        bingo=1
    judge_disp=[[judge_list[i+3*n] for i in range(3)] for n in range(3)] 
    print(*judge_disp,sep="\n")
    return bingo

A_disp=[[A[i+3*n] for i in range(3)] for n in range(3)] 
print(*A_disp,sep="\n")

if bingo_judge(A,b)==1:
    print("yes")
else:
    print("No")

