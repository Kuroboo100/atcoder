def query1(S,iq,cq):
    S_list=list(S)
    S_list[iq-1]=cq
    S="".join(S_list)
    return S

def query2(S,lq,rq):
    chosen=list(set(S[lq-1:rq]))
    return len(chosen)

def main():
    #input
    N=int(input())
    S=input()
    Q=int(input())

    query_list=[]
    for n in range(Q):
        task=input().strip().split()
        if task[0]=="1":
            task[1]=int(task[1])
        elif task[0]=="2":
            task[1]=int(task[1])
            task[2]=int(task[2])
        query_list.append(task)

    #execute
    for n in range(Q):
        if query_list[n][0]=="1":
            S=query1(S,query_list[n][1],query_list[n][2])
        elif query_list[n][0]=="2":
            print(query2(S,query_list[n][1],query_list[n][2]))

main()
    