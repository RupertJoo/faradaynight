def boj_1002():
    n=int(input())
    for _ in range(n):
        from sys import stdin
        x1,y1,r1,x2,y2,r2=map(int,stdin.readline().split())
        r=((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if r1 >= r2: r1, r2 = r2, r1

        if (r2 - r1 < r) and (r < r1 + r2): print(2)
        elif (r == r1 + r2 ) or (r == r2 - r1 and r !=0): print(1)
        elif r < r2-r1 or r > r1+r2: print(0)
        elif r == 0 and r1 == r2: print(-1)
boj_1002()
