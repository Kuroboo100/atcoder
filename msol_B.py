A,B,C=map(int,input().strip().split())
K=int(input())
if A<B and B<C:
    print("Yes")
else:
    i=0
    while i<K:
        if A>=B:
            B*=2
        else:
            C*=2
        if A<B and B<C:
            print("Yes")
            break
        i+=1
    else:
        print("No")
