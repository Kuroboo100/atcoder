import time

t1=time.time()
N=10
#recursion of factorial method
def f(n):
    if n==2:
        return [[1,2],[2,1]]
    else:
        new=[]
        l=f(n-1)
        for e in l:
            base=tuple(e)
            for m in range(len(e)+1):
                e=list(base)
                e.insert(m,n)
                new.append(e)
    return new

c=f(N)
t2=time.time()
print(len(c))
#print(*c,sep="\n")
print(t2-t1)
