def boj_1966():
    from collections import deque
    from sys import stdin

    n_test=int(input())
    for i in range(n_test):
        n,m=map(int,stdin.readline().split())

        dq=deque(map(int,stdin.readline().split()))
        dq_index=deque([0]*n)
        dq_index[m]=1
        count_pop=0

        while 1 in dq_index:
            if dq[0]==max(dq):
                dq.popleft()
                dq_index.popleft()
                count_pop+=1
            else:
                dq.rotate(-1)
                dq_index.rotate(-1)
        print(count_pop)
boj_1966()
