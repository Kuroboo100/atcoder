import math

def divisor(n):
    rt_n=int(math.sqrt(n))
    cnt=0
    for i in range(1,rt_n+1):
        if n%i==0:
            if i**2==n:
                cnt+=1
            else:
                cnt+=2
    return cnt

def main():
    N=int(input())
    ans=0
    for n in range(N+1):
        ans+=n*divisor(n)
    return ans

if __name__=="__main__":
    print(main())