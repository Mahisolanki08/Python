import random

computer_number = random.randint(1,10)

while True :
  user_number = int(input("Enter number (1-10) :"))

  if user_number == computer_number:
    print("Computer Number : ",computer_number)
    print("You Win !!!")

    game = input("Reset or Quit : ").lower()

    if game == "quit" :
      break

    computer_number = random.randint(1,10)

  else :
    print("Computer Number : ",computer_number)
    print("Wrong Guess ! Try Again.")