NK=list(map(int,input().strip().split()))
N=NK[0]
K=NK[1]
H=list(map(int,input().strip().split()))

H.sort()
for n in range(K):
    if H==[]:
        break
    H.pop()

print(sum(H))