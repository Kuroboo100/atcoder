import math

N=int(input())
sqN=int(math.sqrt(N))+1

def f(x,y,z):
    return x**2+y**2+z**2+x*y+y*z+z*x

dp=[0 for n in range(N)]
for x in range(1,sqN):
    for y in range(x,sqN):
        for z in range(y,sqN):
            tmp=f(x,y,z)
            c=len(set([x,y,z]))
            if tmp<=N:
                if c==1:
                    dp[tmp-1]+=1
                elif c==2:
                    dp[tmp-1]+=3
                else:
                    dp[tmp-1]+=6
            else:
                break
for n in range(len(dp)):
    print(dp[n])