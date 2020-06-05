NR=list(map(int,input().strip().split()))
N=NR[0]
R=NR[1]

if N>=10:
    score=R
elif N<10:
    score=R+(100*(10-N))

print(score)