#!/usr/bin/env python3
import time, sys, random, re
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import re
from rich.progress import track

from random import randint
import story

totalstory = story.story()

keyWords = ["demetri", "ivan", "captain","chetnakov","sergei", "island","airlock","crew", "killed","murder","communication","sleep", "americans","death","spy","attack","california"]
indexListPrinted = []
totalWordsIndexEndConditions = set()



def printer(str, style= "bold green"):
  if str == None:
    return
  for letter in str:  
      modded_letter = Text(letter, style)
      print(modded_letter, end="", flush=True)
      time.sleep(0.0001)
      # make time slower later 
  print("\n")


def preamble():
  for i in track(range(20), description="Intercepting message..."):
    time.sleep(0.3)  # Simulate work being done
    
  printer("January 29th, 1983") 
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

def counterOfWordInputted(wordChosen, scrubbed):
  word_counter = 0
  for word in scrubbed:
    if wordChosen == word:
      word_counter += 1
  return word_counter


def getContextSentence(keyword, scrubbed, wordList):
  macroList = []
  scrubbed_two = scrubbed
  numberForTheLoop = counterOfWordInputted(keyword, scrubbed)
  print(numberForTheLoop)
  if numberForTheLoop == 0:
    printer("ERROR: KEYWORD NOT FOUND", style="bold red")
    return
  
  for x in range(numberForTheLoop):
    try:
      wordIndex = scrubbed_two.index(keyword)
      scrubbed_two.pop(wordIndex)
    except:
      printer("ERROR: KEYWORD NOT FOUND", style="bold red")
      return

    # find previous period to see start of last sentence
    printer(f"{keyword} found at index {wordIndex}")

    # go back to find start of last sentence, 3 extra words
    preIndex = wordIndex
    postIndex = wordIndex
    sentence = ""

    while preIndex != -1:

      if re.search("[!?.]", wordList[preIndex]) != None:
        print("punctuation found at index ")
        if preIndex - 2 < 0:
          preIndex = 0
        else:
          preIndex -= 2
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
      sentence += wordList[i] + " "

    #here is where Paul left off
  
    microList = []
    microList.append(sentence)
    microList.append(keyWordCounter(sentence))
    microList.append(wordIndex) 
    microList.append(preIndex)
    microList.append(postIndex)
    macroList.append(microList)
   
  return macroList



def keywordSearch(scrubbed,wordList):
  chosenWord = input("ENTER KEYWORD: ")
  chosenWord = chosenWord.lower()
  return getContextSentence(chosenWord, scrubbed, wordList)

# takes in list of size two lists, with text and count of other keywords associated with it
# chooses word based off probabilty and checks to make sure we haven't already printed
def chooseATextToReturn(macrolist):
  fullCount = 0
  indexList =[]
  for i in range(len(macrolist)):
    fullCount += macrolist[i][1]
    for j in range(macrolist[i][1]):
      indexList.append(i)
  count = 100
  while count > 1:
    chosenNumber = randint(0, fullCount - 1)
    if macrolist[indexList[chosenNumber]][2] not in indexListPrinted:
      indexListPrinted.append(macrolist[indexList[chosenNumber]][2])
      for q in range(macrolist[indexList[chosenNumber]][3], macrolist[indexList[chosenNumber]][4]):
        totalWordsIndexEndConditions.remove(q)
      return macrolist[indexList[chosenNumber]][0]
    count -= 1
  for q in range(macrolist[0][3], macrolist[0][4]):
    totalWordsIndexEndConditions.remove(q)
  return macrolist[0][0]
    
def chooseATextToReturnTwo(macrolist):
  #chooses text to return based on probability of count/total count
  print(macrolist)
  if macrolist == None:
    return
  #maxFinder = 0
  #maxRow = 0
  #for i in range(len(macrolist)):
  #  if maxFinder > macrolist[i][1] and macrolist[i][2] not in indexListPrinted:
  #    maxFinder = macrolist
  #    maxRow = i
  row = randint(0, len(macrolist) - 1)

  for j in range(macrolist[row][3], macrolist[row][4]):
    totalWordsIndexEndConditions.remove(j)
  return macrolist[row][0]


  


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
  totalWords = range(0, len(totalstory))
  storyList = totalstory.split()
  for i in range(len(storyList)):
    totalWordsIndexEndConditions.add(i)
  storyListScrubbed = []
  

  #scrubbing storyList
  for word in storyList:
    word = word.lower()
    word = re.sub("\W","", word)
    storyListScrubbed.append(word)
  
  print(storyListScrubbed)

  #test printing
  # for word in storyList:
  #   print(f"{word} ",end="")

  # print()

  # for word in storyListScrubbed:
  #   print(f"{word} ",end="")

  # print("\n")

  preamble()

  while len(totalWordsIndexEndConditions) > 25:
    printer(chooseATextToReturnTwo(keywordSearch(storyListScrubbed, storyList)))

  reveal()
    

def reveal():
  #create a function that reveals ending text after enough text has been returned
  printer("stuff")
  pass
  


if __name__ == "__main__":
    main()
