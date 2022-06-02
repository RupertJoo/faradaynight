def boj_10866():
    from collections import deque
    from sys import stdin

    n = int(input())
    dq = deque()

    for _ in range(n):
        cmdx = stdin.readline().split()
        if len(cmdx) == 1 : cmd=cmdx[0]
        else: 
            cmd = cmdx[0]
            x = int(cmdx[1])
        size_dq, isempty = len(dq), False
        if size_dq == 0: isempty = True
        if cmd == "push_front": dq.appendleft(x)
        elif cmd == "push_back": dq.append(x)
        elif cmd == "size": print(size_dq)
        elif cmd =="empty": 
            print(int(isempty)) 
        elif cmd == "pop_front":
            if not isempty: print(dq.popleft())
            else: print(-1)
        elif cmd == "pop_back":
            if not isempty: print(dq.pop())
            else: print(-1)
        elif cmd == "front":
            if not isempty: print(dq[0])
            else: print(-1)
        elif cmd == "back":
            if not isempty: print(dq[-1])
            else: print(-1)
boj_10866()
