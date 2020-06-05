K=int(input())

# if K<=10:
#     print(K)
# else:
#     K=K-10
#     lun=[n for n in range(1,10)]
#     i=0

#     for e in lun:

#         a=e%10-1
#         b=e%10
#         c=e%10+1

#         if a>=0:
#             lun.append(10*e+a)
#             i+=1
#             if i>K:
#                 print(lun[-1])
#                 break

#         lun.append(10*e+b)
#         i+=1
#         if i>K:
#             print(lun[-1])
#             break

#         if c<10:
#             lun.append(10*e+c)
#             i+=1
#             if i>K:
#                 print(lun[-1])
#                 break

#別解

queue=[n for n in range(1,10)]

for i in range(K):
    x=queue.pop(0)

    a=x%10-1
    if a>=0:
        queue.append(10*x+a)
    b=x%10
    queue.append(10*x+b)
    c=x%10+1
    if c<10:
        queue.append(10*x+c)
    
print(x)