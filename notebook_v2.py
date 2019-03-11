# -*- coding: cp1252 -*-
# Simple Notebook with External File Access, Time Stamp and Exception Handling

import time, pickle

fileName = "notebook.dat"
notebook = []

try: myFile = open(fileName,"rb")
except Exception:
  myFile = open(fileName,"wb")
  print("No default notebook was found, created one.")
  myFile.close()
else:
  notebook = pickle.load(myFile)
  myFile.close()

while True:

  print("\n(1) Read the notebook")
  print("(2) Add note")
  print("(3) Edit a note")
  print("(4) Delete a note")  
  print("(5) Save and quit\n")

  try: command = int(input("Please select an option: "))
  except Exception: print("\nPlease select a number between 1 and 5!")
  else:

    if (command == 1):
      print("")
      for i in notebook:
        print(i)
      
    elif (command == 2):
      userInput = input("Write a new note: ")
      newEntry = userInput + " ::: " + time.strftime("%X %x")
      print(newEntry)
      notebook.append(newEntry)
      
    elif (command == 3):
      print("The list has", len(notebook), "notes.")
      i = int(input("Which of them will be changed?: ")) - 1
      print(notebook[i])
      userInput = input("Give the new note: ")
      newEntry = userInput + " ::: " + time.strftime("%X %x")
      notebook[i] = newEntry
      
    elif (command == 4):
      print("The list has", len(notebook), "notes.")
      i = int(input("Which of them will be deleted?: ")) - 1
      print("Deleted note", notebook[i])
      del notebook[i]
      
    elif (command == 5):
      print("Notebook saving and shutting down, thank you.")
      myFile = open(fileName,"wb")
      pickle.dump(notebook, myFile)
      myFile.close()
      break

    else: print("\nIncorrect selection.")
