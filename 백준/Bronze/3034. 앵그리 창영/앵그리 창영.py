def boj_3034():
    from sys import stdin
    n,w,h=map(int,stdin.readline().split())
    l=(w**2+h**2)**0.5
    for i in range(n):
        x=int(input())
        if x<=l:
            print("DA")
        else:
            print("NE")
boj_3034()