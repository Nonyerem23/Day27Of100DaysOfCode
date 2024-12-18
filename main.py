import os
import time

import random

def character(name, type):
  print(name)
  print(type)
  return
def health():
  health = (random.randint(1, 6) * random.randint(1, 12) / 2) + 10
  return health
def strength():
  strength = (random.randint(1, 6) * random.randint(1, 12) / 2) + 12
  return strength
print("Character Builder")
time.sleep(1)
os.system("clear")
name = input("Name your legend: ")
type = input("Character Type (Human, Elf, Wizard, Orc): ")
os.system("clear")
print(name)
print(type)
print("HEALTH: ", health())
print("STRENGTH: ", strength())
print("May your name go down in Legend...")