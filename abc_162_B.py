N=int(input())

S=0
for n in range(N+1):
    if n%3==0 or n%5==0:
        pass
    else:
        S+=n

print(S)
