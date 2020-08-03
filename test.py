def gcd(C,D):
    a=min([C,D])
    b=max([C,D])
    tmp=a
    a=b%a
    b=tmp
    if a==0:
        return tmp
    else:
        return gcd(a,b)

print(937510582*419716939)

393489071757148498
314159265358979323