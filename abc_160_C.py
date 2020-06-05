KN=list(map(int,input().strip().split()))
K=KN[0]
N=KN[1]
A_list=list(map(int,input().strip().split()))

Dis_list=[A_list[n]-A_list[n-1] for n in range(1,N)]
Dis_list.append(K-(A_list[N-1]-A_list[0]))

min_distance=K-max(Dis_list)

print(Dis_list)
print(min_distance)
