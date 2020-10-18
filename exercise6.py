num = 1
print(num)
for num in range(1,31):
  divisors=0
  for i in range(1,num+1):
    if num % i == 0:
      divisors +=1
  if divisors > 2:
    print(num)