S=input()

def coffee_judge(S):
    likecoffee=False
    if S[2]==S[3] and S[4]==S[5]:
        likecoffee=True
    
    if likecoffee==True:
        ans="Yes"
    else:
        ans="No"
    return ans

print(coffee_judge(S))