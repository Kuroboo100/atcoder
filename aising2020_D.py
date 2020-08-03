# N=int(input())
# X=list(map(int,list(input())))

N=200000
X=[1 for n in range(N)]

def bd(X):
    ans=0
    for n in reversed(range(len(X))):
        ans+=2**(len(X)-1-n)*X[n]
    return ans
    
def db(N):
    s=[]
    div=N
    fin=False
    while fin==False:
        mod=div%2
        div=div//2
        s.append(mod)
        if div==0:
            fin=True
    return s[::-1]

def rec(X,dec,S):
    n=dec
    if dp.get(n)!=None:
        return dp[n]
    else:
        n%=S
        X=db(n)
        S=sum(X)
        return rec(X,n,S)+1

d=bd(X)
S=sum(X)
dp={}
dp[0]=0
dp[1]=1

for n in range(N):
    if X[n]==0:
        X[n]=1
        d+=2**(N-1-n)
        S+=1
        tmp=rec(X,d,S)
        dp[d]=tmp
        X[n]=0
        d-=2**(N-1-n)
        S-=1
    else:
        X[n]=0
        d-=2**(N-1-n)
        S-=1
        tmp=rec(X,d,S)
        dp[d]=tmp
        X[n]=1
        d+=2**(N-1-n)
        S+=1
    print(tmp)
