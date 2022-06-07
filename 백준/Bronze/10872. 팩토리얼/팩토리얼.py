def factorial(n,fact_n):
  if n<2:
    if fact_n<=1:
      print(1)
      return
    else:
      print(fact_n)
    return
  else:
    fact_n=fact_n*(n-1)
    factorial(n-1,fact_n)    

n=int(input())
fact_n=n
factorial(n,fact_n)