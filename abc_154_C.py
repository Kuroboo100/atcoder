N=int(input())
A=list(map(int,input().strip().split()))

A.sort()
a=-1
ndup=True
for e in A:
    if a==e:
        ndup=False
    else:
        pass
    a=e
if ndup==True:
    print("YES")
else:
    print("NO")


# def binary_search(A,n):
#     find=False
#     start=0
#     end=len(A)
#     if len(A)==1 and A[0]==n:
#         find=True
#     else:
#         while find==False and start<end-1:
#             middle=(start+end)//2
#             if n>A[middle]:
#                 start=middle
#             elif n<A[middle]:
#                 end=middle
#             else:
#                 find=True
#     return find

# l=[]
# dup=False
# for e in A:
#     if binary_search(l,e):
#         dup=True
#         break
#     else:
#         l.append(e)
#         l.sort()

# if dup==False:
#     print("YES")
# else:
#     print("NO")