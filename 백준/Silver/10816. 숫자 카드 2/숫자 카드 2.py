def boj_10816():
    from sys import stdin
    from bisect import bisect_left, bisect_right

    n = int(input())
    list_n = list(map(int,stdin.readline().split()))
    set_n = set(list_n)
    list_n.sort()
    
    m = int(input())
    list_m = list(map(int,stdin.readline().split()))
    
    result_10816=list(map(lambda x: str(bisect_right(list_n,list_m[x])-bisect_left(list_n,list_m[x])) if list_m[x] in set_n else "0",list(range(len(list_m)))))
    print(" ".join(result_10816))
boj_10816()
