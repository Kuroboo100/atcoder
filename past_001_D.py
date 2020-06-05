N=int(input())
A=[int(input()) for n in range(N)]

def dup_check(N,A):
    c=[0 for n in range(N)]
    dup=0

    for nn in range(N):
        for element in A:
            if element==nn+1:
                c[nn]+=1
            else:
                pass

        if c[nn]==2:
            dup=nn+1

    if dup==0:
        return "Correct"
    else:
        for n in range(len(c)):
            if c[n]==0:
                miss=n+1
        temp=(str(dup),str(miss))
        return " ".join(temp)

print(dup_check(N,A))


