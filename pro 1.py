import random
rock = None
paper= None
scissor= None

while True:
  choices = ["rock", "paper", "scissor"]

  computer = random.choice(choices)

  player= None
  
  while player not in choices:
    player = input("rock , paper, scissor: ").lower()

    
  if player== computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")

  elif player== "rock":
    if computer=="paper":
      print("Computer: ",computer)
      print("Player: ",player)
      print("Computer WON!")

    if computer == "scissor":
      print("Computer: ",computer)
      print("Player: ",player)
      print("You WON! Congrats")

  elif player== "paper":
    if computer=="rock":
      print("Computer: ",computer)
      print("Player: ",player)
      print("Computer WON!")

    if computer == "scissor":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You WON! Congrats")

  elif player== "scissor":
    if computer== "rock":
      print("Computer: ",computer)
      print("Player: ",player)
      print("Computer WON!")

    if computer == "paper":
      print("Computer: ",computer)
      print("Player: ",player)
      print("You WON! Congrats")

  play_again = input("Play again (yes/no): ").lower()
  if play_again!= "yes":
    break

print("Bye!")
