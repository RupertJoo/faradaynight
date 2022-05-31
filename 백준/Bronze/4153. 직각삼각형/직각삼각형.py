def boj_4153():
    from sys import stdin
    list_l=list(map(int,stdin.readline().split()))
    while list_l != [0,0,0]:
        list_l.sort()
        if list_l[2]**2==list_l[0]**2+list_l[1]**2:
            print("right")
        else:print("wrong")
        list_l=list(map(int,stdin.readline().split()))
boj_4153()