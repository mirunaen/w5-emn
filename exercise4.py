num1=int(input("Choose a num: "))
num2=int(input("Choose another num:"))
product=num1*num2
sum=0
while sum< product:
  sum +=num1
if product == sum:
  print("num1*num2,product")