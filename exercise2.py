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
    text=int(input("Welcome\n-----------\n1-Deposit\n2-Cash withdrawal\n3-Exit\nChoose the operation: "))
    print("Your balance is: ",balance)
    if text=="2":
      money=int(input("Enter quantity: "))
      if money>balance:
        print("Error.\nThe quantity is greater than the balance.")
      else:
        balance-=money
        print("Your new salary is",balance)
    else:
      if text=="1":
        balance +=int(input("Enter quantity you want to ingress: "))
        print("Your new balance is",balance)
      else:
        print("See you!")