# A=[list(map(int,input().strip().split())) for n in range(3)]
# A_input=[]
# for n in range(3):
#     for m in range(3):
#         A_input.append(A[n][m])
# N=int(input())
# b=[int(input()) for n in range(N)]

def bingo_judge(A_input,b):
    bingo=0
    judge_list=[0,0,0,0,0,0,0,0,0]
    for number in b:
        for i in range(9):
            if number==A_input[i]:
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
    #test display
    judge_disp=[[judge_list[i+3*n] for i in range(3)] for n in range(3)] 
    print(*judge_disp,sep="\n")
    
    return bingo

def main():
    if bingo_judge(A_input,b)==1:
        print("yes")
    else:
        print("No")

#test code
test_time=10
def test_code():
    import random
    A_input=[random.randint(1,10) for n in range(9)]
    N=random.randint(1,10)
    b=[random.randint(1,10) for n in range(N)]
    A_disp=[[A_input[i+3*n] for i in range(3)] for n in range(3)] 
    print(b)
    print(*A_disp,sep="\n")
    print(bingo_judge(A_input,b))

for i in range(test_time):
    test_code()

