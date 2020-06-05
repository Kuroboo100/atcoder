import math

N=int(input())

pos=[]
for n in range(N):
    pos.append(list(map(int,input().strip().split())))

MAX=0
for i in range(N-1):
    for j in range(i+1,N):
        d=(pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2
        if d>=MAX:
            MAX=d

print(math.sqrt(MAX))