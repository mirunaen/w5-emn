"""a = 0
while a >0 and a<5:
  print(5-a,end="")
  a+=1"""
"""
for a in range(0,2):
  print(a)
  for b in range(3,1,-1):
    print(b)
    print(a+b,end=" ")"""
  
"""s="hola soy una cadena de texto"
for letra in s:
  if letra =="a" or letra =="e":
    letra="x"
print(s)
"""
"""
for a in range(-3,2):
  for b in range(0,4):
    for c in range(8,4,-1):
      print("hello")
  
import random
n = random.randrange(1,21)
print(n)
num=int(input("Guess the number between 1 and 20:"))
while num !=n:
  if num <n:
    num=int(input("Too small"))
  else:
    num=int(input("Too big"))
if num == n:
  print("You are correct!Congrats!")

even=30 // 2
print("The num of even number are",even)
"""

import random
a=int(input("Write a num:"))
b=int(input("Write another num:"))
i=0
while a + 5 >= b:
  a=int(input("Write another num:"))
  b=int(input("Write another num:"))
a=random.randint(a,b)
print(a)
while (i<5):
  if a %2==0:
    a=random.randint(a,b)
    if a%2 != 0:
      print(a)
      i +=1
  else:
    a=random.randint(a,b)
    if a%2==0:
      print(a)
      i+=1
        