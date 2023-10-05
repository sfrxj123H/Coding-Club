import os
import sys
import subprocess
import random

x = input("Rock => 1; Paper => 2; Scissors => 3. Your answer: ")
y = random.randint(1, 3)
x = int(x)

if (x == 1 or x == 2 or x ==3):
   chances = ["Rock", "Paper", "Scissors"]
   xText = chances[x - 1]
   yText = chances[y - 1]
else:
   print("Invalid input! Select 1 , 2 or 3 .")
   subprocess.call([sys.executable, os.path.realpath(__file__)] +
   sys.argv[1:])

if ((x == 1) and (y == 2)) or ((x == 2) and (y == 3)) or ((x == 3) and (y == 1)):
   print("You lose!\nYour answer: ", xText, "\nSystem's answer: ", yText, ".");
if ((x == 1) and (y == 3)) or ((x == 2) and (y == 1)) or ((x == 3) and (y == 2)):
   print("You win!\nYour answer: ", xText, "\nSystem's answer: ", yText, ".");
if (x == y):
   print("tie\nYour answer: ", xText, "\nSystem's answer: ", yText, ".");

if (input("Do you want to challenge again? (1 to restart) Your answer: ") == str(1)):
   subprocess.call([sys.executable, os.path.realpath(__file__)] +
   sys.argv[1:])