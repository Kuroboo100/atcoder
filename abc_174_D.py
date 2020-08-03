N=int(input())
c=list(input())

W_cnt=c.count("W")
R_cnt=c.count("R")

wcnt=0
rcnt=0
for n in range(R_cnt):
    if c[n]=="W":
        wcnt+=1
for n in range(R_cnt+1,N):
    if c[n]=="R":
        rcnt+=1
print(max(wcnt,rcnt))



