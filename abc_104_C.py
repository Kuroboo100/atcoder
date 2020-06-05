#AC use dfs bit search
D,G=map(int,input().strip().split())
pc=[]
for _ in range(D):
    pc.append(list(map(int,input().strip().split())))
    
min_num=0
for i in range(D):
    min_num+=pc[i][0]

def dfs(l,D,G):
    global min_num
    score=0
    num=0
    if len(l)==D:
        for n in range(len(l)):
            if l[n]==1:
                score+=pc[n][0]*100*(n+1)+pc[n][1]
                num+=pc[n][0]
        if score>=G:
            min_num=min(min_num,num)
        else:
            for n in reversed(range(len(l))):
                if l[n]==0:
                    i=0
                    while i<=pc[n][0]-1 and score<G:
                        score+=100*(n+1)
                        num+=1
                        i+=1
                    if score>=G:
                        break
            min_num=min(min_num,num)
        return
    else:
        for n in range(2):
            l.append(n)
            dfs(l,D,G)
            l.pop()
dfs([],D,G)
print(min_num)

#AC use bit shift
# =============================================================================
# D,G=map(int,input().strip().split())
# pc=[]
# for _ in range(D):
#     pc.append(list(map(int,input().strip().split())))
# 
# N=0
# for i in range(D):
#     N+=pc[i][0]
# 
# MIN_SUM=N
# for n in range(2**D):
#     score=0
#     SUM=0
#     for i in range(D):
#         if (n>>i)&1==1:
#             SUM+=pc[i][0]
#             score+=100*(i+1)*pc[i][0]+pc[i][1]
#     if score>=G:
#         pass
#     else:
#         for j in reversed(range(D)):
#             if (n>>j)&1==0:
#                 cnt=0
#                 while cnt<=pc[j][0]-2 and score<G:
#                     score+=100*(j+1)
#                     SUM+=1
#                     cnt+=1
#     if score>=G and SUM<=MIN_SUM:
#         MIN_SUM=SUM
# 
# print(MIN_SUM)
# =============================================================================
            
            
            


# =============================================================================
# wrong answer1
# N=0
# for i in range(D):
#     N+=pc[i][0]
# 
# answered=[0 for _ in range(D)]
# score=0
# for i in range(N):
#     MAX=0
#     solved=len(answered)+1
#     for j in range(D):
#         remain=pc[j][0]-answered[j]
#         if remain==1: #bonus point included
#             if MAX<=100*(j+1)+pc[j][1]:
#                 solved=j
#                 MAX=100*(j+1)+pc[j][1]
#         elif remain>=2: #bonus not included
#             if MAX<=100*(j+1):
#                 solved=j
#                 MAX=100*(j+1)
#     score+=MAX
#     answered[solved]+=1
#     if score>=G:
#         break
# 
# print(sum(answered))
# =============================================================================

# =============================================================================
#wrong answer2
#score=0
# num=0
# fin=False
# for i in reversed(range(D)):
#     for j in range(pc[i][0]):
#         score+=100*(i+1)
#         num+=1
#         if j ==pc[i][0]-1:
#             score+=pc[i][1]
#         if score>=G:
#             fin=True
#             break
#     if fin==True:
#         break
# =============================================================================
        

