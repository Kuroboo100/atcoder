X=int(input())

for n in range(200):
    for i in range(-200,200):
        x=i**5-(i-n)**5
        if x==X:
            print(str(i)+" "+str(i-n))
            break