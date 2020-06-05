N=int(input())
S=[input() for n in range(N)]

nondup=list(set(S))
count_list={}
for element in nondup:
    count_list[element]=S.count(element)
count_sorted = sorted(count_list.items(), key=lambda x:x[1], reverse=True)

max_number=0
max_list=[]
for n in range(len(count_sorted)):
    if count_sorted[n][1]>=max_number:
        max_number=count_sorted[n][1]
        max_list.append(count_sorted[n][0])
print(*sorted(max_list),sep='\n')





    
