def binary(a):
    a_bin=[]
    for n in range(len(a)):
        s=[0 for n in range(30)]
        div=a[n]
        fin=False
        p=0
        while fin==False:
            mod=div%2
            div=div//2
            s[p]=mod
            if div==0:
                fin=True
            p+=1
        a_bin.append(s)
    return a_bin
    
def decimal(bin):
    dec=0
    for n in range(len(bin)):
        dec+=bin[n]*2**n
    return dec

def main():
    #input
    N=int(input())
    a=list(map(int,input().strip().split()))

    
if __name__=="__main__":
    main()
