from sys import stdin

n = int(stdin.readline())
set_n = set(map(int,stdin.readline().split()))
m = int(stdin.readline())
list_m = list(map(int,stdin.readline().split()))

results = list(map(lambda x: '1' if x in set_n else '0', list_m))
print(" ".join(results))