import numpy as np
N,M=map(int,input().strip().split())
LR=np.array([list(map(int,input().strip().split())) for _ in range(M)])
print(max(min(LR[:,1])-max(LR[:,0])+1,0))
