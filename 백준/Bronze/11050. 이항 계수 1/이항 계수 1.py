def boj_11050():
    def factorial(n):
        x = 1
        for i in range(1,n+1):x *= i
        return x

    from sys import stdin
    n, k = map(int, stdin.readline().split())

    ans=int(factorial(n) / (factorial(k) * factorial(n-k)))
    print(ans)
boj_11050()