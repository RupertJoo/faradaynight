def boj_2805():
    from sys import stdin
    n, m = map(int,stdin.readline().split())
    list_t = list(map(int,stdin.readline().split()))
    h_start, h_end = 0, max(list_t)
    
    while h_start <= h_end:
        h_mid = (h_start + h_end) // 2
        len_t = 0
        for h in list_t:
            if h - h_mid > 0:
                len_t += h - h_mid
        if len_t < m:
            h_end = h_mid - 1
        else:
            h_start = h_mid + 1
    
    print(h_end)
boj_2805()