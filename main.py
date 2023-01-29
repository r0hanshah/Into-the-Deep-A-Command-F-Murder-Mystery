#!/usr/bin/env python3
import time, sys, random, re
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import re

from random import randint

indexListPrinted = []
keyWords = ["Demetri", "Ivan", "Captain","Chetnakov","Sergei", "Island","Airlock","Crew", "Killed","Murder","Communication","Sleep", "Americans","Death","Spy","Attack","California"]

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
    wordIndex = scrubbed.index(keyword)
  except:
    printer("ERROR: KEYWORD NOT FOUND", style="bold red")
    return

  # find previous period to see start of last sentence
  printer(f"{keyword} found at index {wordIndex}")

  # go back to find start of last sentence, 3 extra words
  preIndex = wordIndex
  postIndex = wordIndex

  while preIndex != -1:

    if re.search("[!?.]", wordList[preIndex]) != None:
      print("punctuation found at index ")
      if preIndex - 2 < 0:
        preIndex = 0
      else:
        preIndex -= 2;
      break

    else:
      preIndex -= 1

  while postIndex != len(wordList):

    if re.search("[!?.]", wordList[postIndex]) != None:
      if postIndex + 4 >= len(wordList):
        postIndex = len(wordList)
      else:
        postIndex += 4
      break

    else:
      postIndex += 1

  print(f"pre-index: {preIndex}, post index: {postIndex}")

  for i in range(preIndex, postIndex):
    print(wordList[i], end=" ")


def keywordSearch(scrubbed,wordList):
  chosenWord = input("ENTER KEYWORD: ")
  getContextSentence(chosenWord, scrubbed, wordList)

# takes in list of size two lists, with text and count of other keywords associated with it
# chooses word based off probabilty and checks to make sure we haven't already printed
def chooseATextToReturn(ListOfPairs):
  fullCount = 0
  indexList =[]
  for i in range(len(ListOfPairs)):
    fullCount += ListOfPairs[i][1]
    for j in range(ListOfPairs[i][1]):
      indexList.append(i)
  count = 100
  while count > 1:
    chosenNumber = randint(0, fullCount - 1)
    if ListOfPairs[indexList[chosenNumber]][2] not in indexListPrinted: 
      return ListOfPairs[indexList[chosenNumber]][0]
    count -= 1
    return ListOfPairs[0][0]
    

def keyWordCounter(s):
  splitList = s.split()
  splitListCleaned = []
  for word in splitList:
    word = word.lower()
    word = re.sub("\W","", word)
    splitListCleaned.append(word)
  counter = 0
  for word in splitListCleaned:
    if word in keyWords:
      counter += 1
  return counter

def main():
  keywords = {"test",}
  story = "yadda yadda yadda important words here. This sentence contains test, the whole thing should be present. These should show, these should not."
  storyList = story.split()
  storyListScrubbed = []

  #scrubbing storyList
  for word in storyList:
    word = word.lower()
    word = re.sub("\W","", word)
    storyListScrubbed.append(word)


  #test printing
  for word in storyList:
    print(f"{word} ",end="")

  print()

  for word in storyListScrubbed:
    print(f"{word} ",end="")

  print("\n")

  # preamble()

  while True:
    keywordSearch(storyListScrubbed, storyList)


main()
