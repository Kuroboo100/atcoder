NK=list(map(int,input().strip().split()))
N=NK[0]
K=NK[1]

for n in range(1,36):
    if N<K**n:
        digit=n
        break
print(digit)