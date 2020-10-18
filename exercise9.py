max=int(input("Introduce the top limit to generate perfect numbers and press Enter"))
sum=0
n=1
for n in range (2,max+1):
  sum=0
  for i in range (1,n):
    if n%i ==0:
      sum +=i
  if sum == n:
    print(n,"is a perfect number")