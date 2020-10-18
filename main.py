#ATM
import random

number=int(random.randrange(1,10000))
balance=random.randrange(50,5000)
print(number)
n=int(input("Enter the 4-digit PIN:"))

i=0
while i<3:
  i=i+1
  if n!=number:
    n=int(input("Enter another pin:"))
  else:
    print("Correct pin")
else:
  print("End")