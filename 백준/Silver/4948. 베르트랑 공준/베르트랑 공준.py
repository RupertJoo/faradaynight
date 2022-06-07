check=False

n=123456*2+1

list_bool=[False]*2+[True]*(n-1)
list_prime=[]

for i in range(2,n+1):
  if list_bool[i]:
    list_prime.append(i)
    for j in range(2*i,n+1,i):
      list_bool[j]=False


while check==False:
  x=int(input())
  if x==0:
    check=True
    break
  else:
    ans=list_bool[x+1:2*x+1].count(True)
    print(ans)
  