def main():
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

if __name__=="__main__":
    main()
    