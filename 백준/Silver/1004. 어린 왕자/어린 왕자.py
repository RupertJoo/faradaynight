def boj_1004():
    from sys import stdin
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int,stdin.readline().split())
        sq_r = (x2 - x1)**2 + (y2 - y1)**2
        count1=0
        count2=0
       
        n = int(input())
        list_p = []
        for _ in range(n):
            list_p.append(list(map(int,stdin.readline().split())))
        # print(list_p)
        for i in list_p:
            if ((i[0]-x2)**2 + (i[1]-y2)**2) > i[2]**2 and ((i[0]-x1)**2 + (i[1]-y1)**2) < i[2]**2:count1+=1 
            if ((i[0]-x1)**2 + (i[1]-y1)**2) > i[2]**2 and ((i[0]-x2)**2 + (i[1]-y2)**2) < i[2]**2:count2+=1 
            
        print(count1+count2)
boj_1004()