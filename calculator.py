# -*- coding: cp1252 -*-
# Simple Calculator with Input Validation

import math

def getInput():
  
  while True:
    try: n = int(input("Input a number: "))
    except Exception: print("This input is invalid.")
    else: return n

def main():
  
  print("Calculator\n")

  n1 = getInput()
  n2 = getInput()

  while True:
    print("\n(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(number1/number2)")
    print("(6) cos(number1/number2)")
    print("(7) Change numbers")
    print("(8) Quit")
    print("Current numbers:", n1, n2)

    try: command = int(input("\nSelect an option (1-8): "))
    except Exception: print("\nPlease select a number between 1 and 8!")
    else:

      if (command == 1): print("\nThe result is: ", n1 + n2)
      elif (command == 2): print("\nThe result is: ", n1 - n2)
      elif (command == 3): print("\nThe result is: ", n1 * n2)
      elif (command == 4): print("\nThe result is: ", n1 / n2)
      elif (command == 5): print("\nThe result is: ", math.sin(n1 / n2))
      elif (command == 6): print("\nThe result is: ", math.cos(n1 / n2))
      elif (command == 7):
        n1 = getInput()
        n2 = getInput()
      elif (command == 8):
        print("Thank you!")
        break
      else: print("\nSelection was not correct.")
  
if __name__ == "__main__":
    main() 
