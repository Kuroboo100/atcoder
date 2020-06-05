# ans-2 (with recursion)

#input
N=int(input())
X=[]
Y=[]
for n in range(N):
    A=int(input())
    lx=[]
    ly=[]
    for m in range(A):
        x,y=map(int,input().strip().split())
        lx.append(x)
        ly.append(y)
    X.append(lx)
    Y.append(ly)    

def judge(l,X,Y):
    honest=True
    for n in range(N):
        if l[n]==1:
            for i in range(len(X[n])):
                if l[X[n][i]-1]!=Y[n][i]:
                    honest=False
    return honest

ans=0
def dfs(l,N): #honest=1,unkind=0
    if len(l)==N:
        global ans
        if judge(l,X,Y):
            ans=max(ans,sum(l))
            return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,N)
            l.pop()

dfs([],N)
print(ans)  



# ans-1 AC (without recursion)
# =============================================================================
# =============================================================================
# #input
# N=int(input())
# 
# g=[[-1 for n in range(N)] for m in range(N)]
# 
# for n in range(N):
#     A=int(input())
#     for m in range(A):
#         x,y=map(int,input().strip().split())
#         g[x-1][n]=y
# =============================================================================

# def c(n,N,base):
#     S=[0 for i in range(N)]
#     for i in range(N):
#         S[i]=n%base
#         n=n//base
#     return S
# 
# 
# def honest_judge(S,g):
#     honest=True
#     for n in range(len(S)):
#         if S[n]==1:
#             for i in range(N):
#                 if g[i][n]!=-1 and g[i][n]!=S[i]:
#                     honest=False
#         if honest==False:
#             break
#     return honest
# 
# MAX=0
# for n in range(2**N):
#     S=c(n,N,2)
#     if honest_judge(S,g)==True:
#         if sum(S)>=MAX:
#             MAX=sum(S)
# print(MAX)
# =============================================================================


    


