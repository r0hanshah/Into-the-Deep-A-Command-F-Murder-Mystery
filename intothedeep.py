#!/usr/bin/env python3
import time, sys, random, re
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from rich.align import Align
import copy
from random import randint
import story

import os, signal

totalstory = story.story()

keyWords = ["demetri", "ivan", "captain","chetnakov","sergei", "island","airlock","crew", "killed","murder","communication","sleep", "americans","death","spy","attack","california", "murdered"]
indexListPrinted = []
totalWordsIndexEndConditions = set()


def print_ascii_art(art, delay=0.05):
    console = Console()
    lines = art.split('\n')
    for line in lines:
        console.print(Align(line, align= "center"))
        time.sleep(delay)

def printer(str, style= "bold green"):
  if str == None:
    return
  for letter in str:  
      modded_letter = Text(letter, style)
      print(modded_letter, end="", flush=True)
      time.sleep(0.05)
      # make time slower later 
  print("\n")


def preamble():
  print(Panel(Align("Into the [blue]Deep[/blue]: A Control-F [red]MURDER MYSTERY", align= "center")))
  time.sleep(0.03)
  
  for i in track(range(20), description="Intercepting message..."):
    time.sleep(.18)  # Simulate work being done


  print_ascii_art("""\
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣧[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣼⣿⡆[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢠⣿⠻⣿⡀[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣾⠇⠀⢻⣇[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠲⣶⣶⣶⣶⣶⣶⣶⣾⡿⠀⠀⠈⣿⣶⣶⣶⣶⣶⣶⣶⡶⠆[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠈⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠈⠛⢿⣦⡄⠀⠀⠀⠀⠀⢠⣶⠿⠋[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢰⡿⠀⠀⠀⡀⠀⠀⠘⣿⡄[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[red]⣀⡤[/red]⠀⠀⠀⠀⠀⠀⠀[yellow]⢀⣿⠃⢀⣴⡾⠿⣷⣄⡀⢹⣷[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⢦⣄⡀[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀[red]⢀⣀⣴⣿⠋[/red]⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣼⣿⣶⠟⠋⠀⠀⠈⠙⢿⣶⣿⣇[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⠙⢿⣶⣄⣀[/red]⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀[red]⣠⡾⢹⣿⠟⡅[/red]⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣰⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⡄[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⢨⡻⣿⡎⢿⣆[/red]⠀⠀⠀⠀
⠀⠀[red]⢀⢶⣿⠇⣟⣥⡾⠁[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠲⢤⣄⠀⠀⠀⠀⠁[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀[red]⢻⣮⣻⠸⣿⡷⣄[/red]⠀⠀
⠀[red]⢠⡟⢸⣿⣴⣿⠏[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠙⢿⣶⣤⡀[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[red]⢹⣿⣶⣿⡇⢹⡄[/red]⠀
⠀[red]⣾⣷⢸⡿⣋⣴⠁[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢀⣤⣤⣄⣀⠀⠀⠀⠀⠈⢿⣿⣦⡀[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀⠀[red]⢷⣍⢻⡇⣿⣷[/red]⠀
⠀[red]⣿⣿⠘⣷⣿⠃[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢀⣴⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠹⣿⣿⣦[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀[red]⠘⢿⣷⡀⣿⣿⢀[/red]
[red]⣧⠸⣿⣼⡿⣣[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢀⣴⣿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣧[/yellow]⠀⠀⠀⠀⠀⠀⠀⠀[red]⣌⠻⣿⣿⠇⣼[/red]
[red]⣿⡆⢹⡟⣰⡿[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠙⢿⣿⠟⠉⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡇[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⢹⣦⠹⡿⢠⣿[/red]
[red]⢻⣿⡄⢰⣿⠇[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠁⠀⠀⠀⠀⠹⣿⣷⣦⡀⠀⠀⠀⠀⠀⣸⣿⣿⣧[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⠈⣿⣧⢀⣿⡟[/red]
[red]⡌⢿⣷⣾⡿⢠[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⠻⣿⣿⣦⡀⠀⠀⠀⣿⣿⣿⡿[/yellow]⠀⠀⠀⠀⠀⠀⠀[red]⣏⢹⣿⣾⡿⢁[/red]
[red]⣷⡌⢻⣿⡇⣼⡇[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⣀⡀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⣀⣼⣿⣿⣿⠇[/yellow]⠀⠀⠀⠀⠀⠀[red]⢰⣿⠀⣿⠟⢡⣾[/red]
[red]⠘⣿⣦⡙⠃⣿⡇⡀[/red]⠀⠀⠀⠀⠀⠀⠀⠀[yellow]⢰⣿⡿⢿⣿⣶⣤⣀⣀⠀⠀⠀⣈⣻⣿⣿⣿⣿⣿⠏[/yellow]⠀⠀⠀⠀⠀⠀[red]⢀⢸⣿⠀⢫⣴⣿⠃[/red]
⠀[red]⢸⣿⣿⣦⣿⣇⢸⣆[/red]⠀⠀⠀⠀[yellow]⢀⣠⣾⡿⠉⠁⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀[/yellow]⠀⠀⠀⠀⠀[red]⣰⡏⢸⣿⣴⣿⠟⡁[/red]⠀
⠀[red]⠈⢧⣉⠻⢿⣿⠀⣿⣆[/red]⠀⠀[yellow]⢠⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠋⠉⠉⠻⣿⣿⡆[/yellow]⠀⠀⠀[red]⣰⣿⠁⣾⡿⠟⣡⡼⠁[/red]⠀
⠀⠀[red]⠈⠻⣷⣤⣙⠃⢹⣿⡖⣄⡀[/red][yellow]⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉[/yellow]⠀⠀[red]⣠⢲⣿⡟⢈⣩⣴⣾⠟⠁[/red]⠀⠀
⠀⠀⠀⠀[red]⠈⢻⣿⣿⣦⣿⣿⡌⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⢃⣾⣿⣶⣿⡿⡟⠁[/red]⠀⠀⠀⠀
⠀⠀⠀⠀⠀[red]⠈⠳⣬⣉⣙⣛⠛⠎⠻⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟⣁⣚⣛⣉⣩⣤⠞⠁[/red]⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀[red]⠈⠙⢻⡿⣿⣿⡿⠿⠿⠟⢛⣩⣤⣶⡶⠖⣲⣶⢶⣶⡚⠶⣶⣶⣙⡛⠻⠿⠿⠿⠿⠿⡟⠋⠁[/red]⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[red]⠑⢶⣤⣤⣴⣶⣾⣿⡿⠟⣉⣴⠟⠉⠀⠀⠈⠻⢷⣌⡙⠿⣿⣿⣷⣶⣶⣶⡶⠚⠁[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[red]⠉⠉⠉⠉⠀⠠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⡦⠀⠈⠉⠉⠉[/red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
  
    
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
  if keyword == "superior":
    printer("ERROR: KEYWORD NOT FOUND", style="bold red")
    return
  macroList = []
  scrubbed_two = copy.deepcopy(scrubbed)
  numberForTheLoop = counterOfWordInputted(keyword, scrubbed)
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

    # go back to find start of last sentence, 3 extra words
    preIndex = wordIndex
    postIndex = wordIndex
    sentence = ""

    while preIndex != -1:

      if re.search("[!?.]", wordList[preIndex]) != None:
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

    # print(f"pre-index: {preIndex}, post index: {postIndex}")

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
  if macrolist == None:
    return
  fullCount = 0
  indexList =[]
  counterForEndCondition = 0
  for i in range(len(macrolist)):
    fullCount += macrolist[i][1]
    for j in range(macrolist[i][1]):
      indexList.append(i)
  count = 10
  while count > 1:
    chosenNumber = randint(0, fullCount - 1)
    if macrolist[indexList[chosenNumber]][2] not in indexListPrinted:
      indexListPrinted.append(macrolist[indexList[chosenNumber]][2])
      for q in range(macrolist[indexList[chosenNumber]][3], macrolist[indexList[chosenNumber]][4]):
        try:
          totalWordsIndexEndConditions.remove(q)
        except: 
          waster = ""
      return macrolist[indexList[chosenNumber]][0]
    count -= 1
  for q in range(macrolist[0][3], macrolist[0][4]):
    try:
      totalWordsIndexEndConditions.remove(q)
    except:
      waster = "wasted"
  if counterForEndCondition == 0:
    counterForEndCondition += 1
    return macrolist[0][0]
  else:
    return "All instances of this keyword have been exhausted."

  
  


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
  


  preamble()

  while len(totalWordsIndexEndConditions) > 250:
    printer(chooseATextToReturn(keywordSearch(storyListScrubbed, storyList)))
  

  reveal()
  
  os.kill(os.getppid(), signal.SIGHUP)
    

def reveal():
  #create a function that reveals ending text after enough text has been returned
  printer("It's all over.\nAs the last of the surplus rations disappeared, the captain's mysterious disappearance marked the beginning of the end for our crew.\nOur spirits sank as our supply of spirits dwindled, and Demetri's fits of hysteria grew wilder by the day. I knew something was off about him, so one night I decided to sneak into his chambers and investigate. \n\nAs I sifted through his chests, I found tomes written in foreign tongues, but no signs of his family. Strange symbols resembling heinous fish beasts adorned the pages. And then, hidden in plain sight, I saw it - the captain's pocket watch. It was clear to me that Demetri had killed Chetnakov. But as I made my escape, the floorboards beneath me creaked, alerting Demetri to my presence. He awoke in a rage, screaming and cursing. \n\nI fled for my life, slamming the door shut behind me, but he tore it open with ease. I made it to the captain's room, where Ivan and Sergei were waiting for me. We locked ourselves inside, but Demetri was breaking down the door with manic strength. He screamed about throwing us out of the airlock. We knew we couldn't overpower him. As I write this, the door is about to give way. My fate, and that of my crewmates, is uncertain. But I had to leave this warning for whoever may come across this -mfeouhfo iwrhfvhfw whoiufDwfWHUPdufvsgvh n.fgyuiwot")
  
  printer("Sharon Sterling arises from the computer with the true knowledge of what happened that fateful night.")
  printer("She exits the submarine, and the ship's computer interface shuts down forever.")
  for i in track(range(20), description="Self Destructing..."):
    time.sleep(.08)  # Simulate work being done
  


if __name__ == "__main__":
    main()
