#!/usr/bin/env python3
import time, sys, random, re
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from random import randint


def printer(str, style= "bold green"):
    for letter in str:  
        modded_letter = Text(letter, style)
        print(modded_letter, end="", flush=True)
        time.sleep(0.001)
        # make time slower later 
    print("\n")


def preamble():
  printer("January 29th, 2023") 
  printer("The Santa Monica pier bustles with its usual beach bodies. As the tide of the Pacific recedes, a large metal object is revealed. \nWithin minutes, local news has arrived to capture the scene. A K-278 Komsomolets Soviet submarine has washed ashore in California.")
  printer("There is no one inside. \nNo clothing, no bodies, no scatter of papers, no trace of any life.")
  printer("You are investigative reporter, Sharon Sterling. \nDucking under the police tape, you make your way to the scene. Just as reported, there is no evidence inside.")
  printer("All that remains is the ship's computer interface. Incredibly, it still boots up when you click the power button. \nYou take your place in front of the screen. What happened to this ship? To the crew? It all rests on you to find out.")
  username = Text("ENTER USERNAME", style= "bold red")
  password = Text("ENTER PASSWORD", style= "bold red")
  askUsername = Prompt.ask(username)
  askPassword = Prompt.ask(password)

  printer("\nINCORRECT USERNAME OR PASSWORD", style= "bold red")
  printer("CONCEALING AND ENCRYPTING CREW LOGS")
  printer("FOR THE PROTECTION OF STATE SECRETS, CREW LOGS ARE ONLY AVAILABLE THROUGH KEYWORD SEARCH. WORKERS OF THE WORLD, UNITE.")

def getContextSentence(keyword, scrubbed, wordList):
  try:
    wordIndex = wordList.index(keyword)
  except:
    printer("ERROR: KEYWORD NOT FOUND", style="bold red")
    return

  # find previous period to see start of last sentence
  printer(f"{keyword} found at index {wordIndex}")

def keywordSearch(scrubbed,wordList):
  chosenWord = input("ENTER KEYWORD: ")
  getContextSentence(chosenWord, scrubbed, wordList)

def chooseATextToReturn(ListOfPairs):
  fullCount = 0
  indexList =[]
  for i in range(len(ListOfPairs)):
    fullCount += ListOfPairs[i][1]
    for j in range(ListOfPairs[i][1]):
      indexList.append(i)
  chosenNumber = randint(0, fullCount - 1)
  return ListOfPairs[chosenNumber][1]
  
def main():
  keywords = {"test",}
  story = "yadda yadda yadda important words here. This sentence contains test, the whole thing should be present. These should show, these should not."
  storyList = story.split()
  storyListScrubbed = storyList

  for word in storyListScrubbed:
    print(word)
    word = word.lower()
    word = re.sub("\W","", word)
    print(f"scrubbed: {word}")


  # preamble()
  keywordSearch(storyListScrubbed, storyList)


main()
