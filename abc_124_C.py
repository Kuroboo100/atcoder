S=list(input())
cnt=0
for n in range(1,len(S)):
    if S[n]==S[n-1]:
        if S[n]=="1":
            S[n]="0"
        else:
            S[n]="1"
        cnt+=1
print(cnt)