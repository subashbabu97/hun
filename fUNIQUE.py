n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(n):
  for j in range(i+1,n-1):
      if x[i]==x[j]:
        print(x[i],end=' ')
        c=c+1
if c==0:
  print("unique")
