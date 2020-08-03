def main_():#見苦しい実装
    #input
    N=int(input())
    l=list("zabcdefghijklmnopqrstuvwxy")
    if N<26:
        print(l[N])
    else:
        name=[]
        n=N
        while n>=26:
            mod=n%26
            if mod!=0:
                n//=26
            else:
                n//=26
                n-=1
            name.append(l[mod])
        if n!=0:
            name.append(l[n])
        name=[name[n] for n in reversed(range(len(name)))]
        print("".join(name))
    

def main():#やり直し
    #input
    N=int(input())
    l=list("abcdefghijklmnopqrstuvwxyz")
    n=N
    name=""
    while n>=26:
        n-=1
        name+=l[n%26]
        n//=26
    if n!=0:
        name+=l[n-1]
    print(name[::-1])

if __name__=="__main__":
    main()
    