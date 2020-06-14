import math

def prime(x):
    if x==1:
        prime=True
        #この問題に合わせて１でもTrueとする
    else:
        prime=True
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i==0:
                prime=False
                break
    return prime

def main():
    #input
    N=int(input())
    A=list(map(int,input().strip().split()))

    A.sort(reverse=True)
    
    #割り切れた場合+1
    cnt=0
    for i in range(N-1):
        #A[i]が素数または1の場合
        if prime(A[i]):
            #前後に同じ数がない場合、割り切れない
            if i<N-1:
                if A[i]==A[i+1]:
                    cnt+=1
            elif i>0:
                if A[i]==A[i-1]:
                    cnt+=1
        #A[i]が素数ではない場合
        else:
            for j in reversed(range(i+1,N)):
                if A[i]%A[j]==0:
                    cnt+=1
                    break
    if A[-1]%A[-2]==0:
        cnt+=1
    print(N-cnt)

if __name__=="__main__":
    main()

s
N=int(input())
A=list(map(int,input().strip().split()))

A.sort()
cnt=0
div=[]
for n in range(1,N):
    for i in range(len(div)):
        if div==[]:
            for m in range(n-1):
                if A[n]%A[m]==0:
                    cnt+=1
                    div.append(A[m])
        else:
            for i in range(len(div)):
                if A[n]%div[i]==0:
                    cnt+=1
                    div.append(A[m])
print(N-cnt)

