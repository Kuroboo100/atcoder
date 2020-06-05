disp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
R,C=map(int,input().strip().split())
sx,sy=map(int,input().strip().split())
gx,gy=map(int,input().strip().split())
c=[]
for n in range(R):
    c.append(list(input()))
s_p=[sx-1,sy-1]
g_p=[gx-1,gy-1]

def BFS(c,s_p,g_p,disp):
    queue=[s_p]
    goal=False
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    i=0
    while queue!=[] and goal==False:
        exe=queue.pop(0)
        c[exe[0]][exe[1]]=disp[i]
        for n in range(4):
            exe_new=[exe[0]+dx[n],exe[1]+dy[n]]
            if exe_new==g_p:
                goal=True
                c[exe_new[0]][exe_new[1]]="*"
                break
            elif c[exe_new[0]][exe_new[1]]=="." and exe_new not in queue:
                queue.append(exe_new)
        i+=1
    return goal,i,c

res=BFS(c,s_p,g_p,disp)
if res[0]==True:
    print(res[1])
else:
    print("no goal")

for e in res[2]:
    print("".join(e))
