#atcoder abc-165-B
X=int(input())

n=100
i=0
while n<X:
    n=int(n*101//100)
    i+=1
    
print(i)


