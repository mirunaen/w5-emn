n=input("Enter a num:")
while n.isdigit() == False and "." not in n:
  n=input("Write a num:")
n=float(n)
print(n**2)