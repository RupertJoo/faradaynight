def boj_1358():
    from sys import stdin

    w,h,x,y,p = list(map(int,stdin.readline().split()))
    c = 0
    pp=[]
    
    for _ in range(p): pp.append(list(map(int,stdin.readline().split())))
    
    for i in pp:
        if x <= i[0] and i[0] <= x + w and y <= i[1] and i[1] <= y + h: c+=1
        elif i[0] < x and (x - i[0])**2 + (y + 0.5 * h - i[1])**2 <= 0.25 * h**2: c+=1
        elif i[0] > x + w and (x + w - i[0])**2 + (y + 0.5 * h - i[1])**2 <= 0.25 * h**2: c+=1
    
    print(c)
boj_1358()