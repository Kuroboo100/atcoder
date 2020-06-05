X=int(input())

def gold_calc(X):
    g_500=0
    g_5=0

    while X>=500:
        X-=500
        g_500+=1000

    while X>=5:
        X-=5
        g_5+=5
    
    return g_500+g_5

print(gold_calc(X))

