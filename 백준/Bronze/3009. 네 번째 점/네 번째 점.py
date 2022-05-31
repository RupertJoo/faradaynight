def boj_3009():
    from sys import stdin
    list_xy=[]

    for i in range(3):
        xy=list(map(int,stdin.readline().split()))
        list_xy.append(xy)

    x1=min(list_xy[0][0],list_xy[1][0],list_xy[2][0])
    x2=max(list_xy[0][0],list_xy[1][0],list_xy[2][0])
    y1=min(list_xy[0][1],list_xy[1][1],list_xy[2][1])
    y2=max(list_xy[0][1],list_xy[1][1],list_xy[2][1])

    list_vertex=[[x1,y1],[x1,y2],[x2,y1],[x2,y2]]

    for i in list_vertex:
        if i not in list_xy:
            print(i[0],i[1])
            break
boj_3009()