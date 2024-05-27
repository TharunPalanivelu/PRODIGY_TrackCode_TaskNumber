import random
print("Welcome to the guessing game\n")

guess=random.randint(1,100)
attempt=0
game=True
while game :
  attempt+=1
  user_guess=int(input("enter a number :"))
  
  if user_guess<guess:
    print("too low")
  elif user_guess>guess:
    print("too high")
  else:
    print("your guess is correct")
    print(f"the number of attempts u made {attempt}")
    game=False