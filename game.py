# -*- coding: cp1252 -*-
# Foot-Nuke-Cockroach Game

import random

def getRandom():
  
  choice = random.randint(1,3)
  if choice == 1: choice = "Foot"
  if choice == 2: choice = "Nuke"
  if choice == 3: choice = "Cockroach"
  return choice

def main():
  
  counter = 0
  wins = 0
  ties = 0

  while True:
    
    player = input("Foot, Nuke or Cockroach? (Quit ends): ")
    
    if player == "Quit":
      print("You played", counter,"rounds, and won", wins, "rounds, playing tie in",  ties, "rounds.")
      break
    
    if player not in ["Foot", "Nuke", "Cockroach"]:
      print("Incorrect selection.")
      continue
    
    computer = getRandom()
    counter += 1

    print("You chose:", player)
    print("Computer chose:", computer)

    if (player == computer) and (player != "Nuke"):
      ties += 1
      print("It is a tie!")
    elif (player == computer) and (player == "Nuke"):
      print("Both LOSE!")
      
    elif player == "Foot" and computer == "Nuke":
      print("You LOSE!")
    elif player == "Foot" and computer == "Cockroach":
      wins += 1
      print("You WIN!")
    elif player == "Nuke" and computer == "Foot":
      wins += 1
      print("You WIN!")    
    elif player == "Nuke" and computer == "Cockroach":
      print("You LOSE!")
    elif player == "Cockroach" and computer == "Foot":
      print("You LOSE!")
    elif player == "Cockroach" and computer == "Nuke":
      wins += 1
      print("You WIN!")

if __name__ == "__main__":
    main()
