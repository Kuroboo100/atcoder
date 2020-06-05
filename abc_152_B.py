ab=list(map(int,input().strip().split()))
a=ab[0]
b=ab[1]

if a<=b:
    print(int(str(a)*b))
else:
    print(int(str(b)*a))