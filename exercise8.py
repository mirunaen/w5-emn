text1=str(input("Is number greater than or less than 5? (greater / less)"))
text2=str(input("Even or odd number? (odd / even)"))
text3=str(input("Upper or lower bound? (upper / lower)"))
num=0
while text1=="greater":
  num=[6,7,8,9,10]
  if num%2==0:
    num=num%2
    if text3=="lower":
      print(num[0])
    else:
      print(num[2])
else:
    num=[6,7,8,9,10]
    if num%2==0:
      num=num%2
      if text3=="lower":
        print(num[0])
      else:
        print(num[2])
    