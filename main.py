import time, sys, random  

from random import randint

def cthulu():
  print("")

def printer(str):
    for letter in str:  
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)
        # make time slower later 
    print("\n")


def preamble():
  printer("January 29th, 2023") 
  printer("The Santa Monica pier bustles with its usual beach bodies. As the tide of the Pacific recedes, a large metal object is revealed. \nWithin minutes, local news has arrived to capture the scene. A K-278 Komsomolets Soviet submarine has washed ashore in California.")
  printer("There is no one inside. \nNo clothing, no bodies, no scatter of papers, no trace of any life.")
  printer("You are investigative reporter, Sharon Sterling. \nDucking under the police tape, you make your way to the scene. Just as reported, there is no evidence inside.")
  printer("All that remains is the ship’s computer interface. Incredibly, it still boots up when you click the power button. \nYou take your place in front of the screen. What happened to this ship? To the crew? It all rests on you to find out.")
  username = input("INPUT USERNAME: ")
  password = input("INPUT PASSWORD: ")

  printer("\nINCORRECT USERNAME OR PASSWORD")
  printer("CONCEALING AND ENCRYPTING CREW LOGS")
  printer("FOR THE PROTECTION OF STATE SECRETS, CREW LOGS ARE ONLY AVAILABLE THROUGH KEYWORD SEARCH. WORKERS OF THE WORLD, UNITE.")

def keywordSearch():
  chosenWord = input("ENTER KEYWORD: ")


#






preamble()
keywordSearch()

#!/usr/bin/env python3




