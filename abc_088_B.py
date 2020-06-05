def main():
    N=int(input())
    a=list(map(int,input().strip().split()))
    
    a.sort(reverse=True)
    
    alice=sum(a[n] for n in range(N) if n%2==0)
    bob=sum(a[n] for n in range(N) if n%2==1)
    return alice-bob

if __name__=="__main__":
    print(main())
    

    