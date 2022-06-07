def iP(x):
  if x==2 or x==3: return x
  if x<2 or x%2==0: return 0
  for i in range(3,int(x**0.5)+1,2):
    if x%i==0:
      return 0   
  return x


def nP(x):
  check=False
  iter=0
  if x<2:return 2
  if x==2:return 3
  
  while check==False and iter<100:
    iter+=1
    x=x+2
    if iP(x)!=0:
      check==True
      return x


def solve():
  M,N=input().split(' ')
  M=int(M)
  N=int(N)
  if M==N and iP(M)!=0: return print(M)
  if M==N and iP(M)==0: return 
  
  for i in range(M,N+1):
    if iP(i)==i:
      print(i)
    else:()
solve()