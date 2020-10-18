import random
n = random.randrange(1,21)
num=int(input("Guess the number between 1 and 20:"))
while num !=n:
  if num <n:
    num=int(input("Too small"))
  else:
    num=int(input("Too big"))
if num == n:
  print("You are correct!Congrats!")