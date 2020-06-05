def q1(c,cn,x):
    print(c[x-1])
    for i in range(len(cn[x-1])):
        c[cn[x-1][i]-1]=c[x-1]

def q2(c,cn,x,y):
    print(c[x-1])
    c[x-1]=y

def main():
    N,M,Q=map(int,input().strip().split())
    uv=[list(map(int,input().strip().split())) for n in range(M)]
    c=list(map(int,input().strip().split()))

    cn=[[] for _ in range(N)]
    for m in range(M):
        cn[uv[m][0]-1].append(uv[m][1])
        cn[uv[m][1]-1].append(uv[m][0])

    for n in range(Q):
        s=list(map(int,input().strip().split()))
        if s[0]==1:
            q1(c,cn,s[1])
        else:
            q2(c,cn,s[1],s[2])

if __name__=="__main__":
    main()

