def fac(n):
    P=10**9+7
    f=1
    for i in range(1,n+1):
        f*=i
        f%=P
    return f

def main():
    X,Y=map(int,input().strip().split())
    if (2*X-Y)%3==0 and (2*Y-X)%3==0:
        a=(2*X-Y)//3
        b=(2*Y-X)//3
        return fac(a+b)//fac(a)//fac(b)
    else:
        return 0    

if __name__=="__main__":
    print(main())
