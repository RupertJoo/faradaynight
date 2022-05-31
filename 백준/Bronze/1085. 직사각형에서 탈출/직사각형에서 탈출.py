def boj_1085():
    from sys import stdin
    x,y,w,h=map(int,stdin.readline().split())
    
    if x<=0.5*w:
        ans_x=x
    else:
        ans_x=w-x
    
    if y<=0.5*h:
        ans_y=y
    else:
        ans_y=h-y
    
    print(min(ans_x,ans_y))

boj_1085()