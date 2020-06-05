import math

def main():
    A,B,H,M=map(int,input().strip().split())
    round_hour=12*60
    round_min=60
    
    #digree to radian
    degree_hour=(60*H+M)/round_hour*360
    degree_min=M/round_min*360
    radian_hour=math.radians(degree_hour)
    radian_min=math.radians(degree_min)
    
    #distance
    d1=A*math.cos(radian_hour)-B*math.cos(radian_min)
    d2=A*math.sin(radian_hour)-B*math.sin(radian_min)
    
    return math.sqrt(d1**2+d2**2)

if __name__=="__main__":
    print(main())
