n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(n):
  for j in range(i+1,n-1):
      if a[i]==a[j]:
        print(a[i],end=' ')
        b=b+1
if b==0:
  print("unique")
