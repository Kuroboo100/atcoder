def check(a,C):
    vertical=False
    horizonal=False
    #vertical
    d1=C[a[0]][0]-C[a[1]][0]
    d2=C[a[0]][1]-C[a[1]][1]
    d3=C[a[0]][2]-C[a[1]][2]
    if d1==d2==d3:
        vertical=True
    #horizonal
    d4=C[0][a[0]]-C[0][a[1]]
    d5=C[1][a[0]]-C[1][a[1]]
    d6=C[2][a[0]]-C[2][a[1]]
    if d4==d5==d6:
        horizonal=True
    return vertical and horizonal    

def main():
    ans=True
    C=[list(map(int,input().strip().split())) for _ in range(3)]
    x=(0,1),(0,2),(1,2)
    for e in x:
        if check(e,C)==False:
            ans=False
            break            
    return "Yes" if ans else "No"

if __name__=="__main__":
    print(main())
    