
def boj_2477():
    from sys import stdin
    from collections import deque

    density=int(input())
    list_v=[]
    for i in range(6):
        list_v.append(list(map(int,stdin.readline().split())))
    
    list_c=[0,0,0,0]
    for j in range(6):
        list_c[list_v[j][0]-1]+=1

    dq=deque(list_v)
    if list_c==[1,2,1,2]:
        while dq[0][0]!=1:
            dq.rotate(-1)
        if dq[1][0]==3:
            area=dq[0][1]*dq[1][1]-dq[3][1]*dq[4][1]
        else: 
            area=dq[0][1]*dq[-1][1]-dq[2][1]*dq[3][1]
    
    elif list_c==[1,2,2,1]:
        while dq[0][0]!=1:
            dq.rotate(-1)
        if dq[1][0]==4:
            area=dq[0][1]*dq[1][1]-dq[3][1]*dq[4][1]
        else: area=dq[0][1]*dq[-1][1]-dq[2][1]*dq[3][1] 
    
    elif list_c==[2,1,1,2]:
        while dq[0][0]!=2:
            dq.rotate(-1)
        if dq[1][0]==3:
            area=dq[0][1]*dq[1][1]-dq[3][1]*dq[4][1]
        else: area=dq[0][1]*dq[-1][1]-dq[2][1]*dq[3][1] 
    
    elif list_c==[2,1,2,1]:
        while dq[0][0]!=2:
            dq.rotate(-1)
        if dq[1][0]==4:
            area=dq[0][1]*dq[1][1]-dq[3][1]*dq[4][1]
        else: area=dq[0][1]*dq[-1][1]-dq[2][1]*dq[3][1]    
    
    n_melon=density*area
    print(n_melon)

boj_2477()