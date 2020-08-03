W,H,x,y=map(int,input().strip().split())

a=W*H/2
if x==W/2 and y==H/2:
    b=1
else:
    b=0

print(str(a)+" "+str(b))