from collections import deque

N=int(input())
h=list(map(int,input().strip().split()))

cnt=0
l=deque([h])
bot=deque([0])
while len(l)>0:
    tmp=l.popleft()
    b=bot.popleft()
    cnt+=min(tmp)-b
    g=deque([n for n in range(len(tmp)) if tmp[n]==min(tmp)])
    g.appendleft(-1)
    g.append(N)
    
    for i in range(1,len(g)):
        if len(tmp[g[i-1]+1:g[i]])>0:
            l.append(tmp[g[i-1]+1:g[i]])
            bot.append(min(tmp))

print(cnt)




            

