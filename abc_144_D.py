import math

a,b,x=map(int,input().strip().split())

if x<=a**2*b/2:
    h=x/a/b*2
    theta=math.atan(b/h)*180/math.pi
else:
    h=2/(a**2)*(a**2*b-x)
    theta=math.atan(h/a)*180/math.pi

print(theta)

