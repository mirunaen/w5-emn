# Create a program that asks the user to enter a number and keeps asking until a number is introduced. 
n=input("Enter a num:")
while n.isdigit() == False and "." not in n:
  n=input("Write a num:")
n=float(n)
print(n**2)