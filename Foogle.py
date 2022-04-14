# Foogle program by Alex Tomsovic
# This project is not related with google.com or Alphabet in any way.

# Libraries
import requests
import os
import time, os, random, sys
from time import sleep
from colorama import Fore,Back,Style

# Google search library
try:
  from googlesearch import search
except:
  os.system("pip install googlesearch-python")
  from googlesearch import search


# Spacers 
spacer1 = "                          "
spacer2 = "                     "
spacer3 = "                "
spacer4 = "              "
spacer5 = "            "
spacer6 = "                                      "

# About header
abouts = f"""{spacer1} {Fore.BLUE}A{Fore.RED}B{Fore.LIGHTYELLOW_EX}O{Fore.BLUE}U{Fore.LIGHTGREEN_EX}T"""

# Logo header
logo = f"{spacer1}"+f"{Fore.BLUE}F{Fore.RED}o{Fore.LIGHTYELLOW_EX}o{Fore.BLUE}g{Fore.LIGHTGREEN_EX}l{Fore.RED}e\n"

wiki_logo = f"{spacer1}"+f"🌐 Wikipedia"

urban_logo = f"{spacer1}"+f"📚 Urban Dictionary"

suggestion_logo = f"{spacer4}"+f"📧 Suggestion or Feedback"


# Functions
def clearpage():
  os.system("cls||clear")

def sp(str): 
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)
  print()

def type(str): 
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.025)
  print()
  
# Home page 
def home_page():
  clearpage()

  print(logo)

 
  print(spacer3+f"{Fore.WHITE}Type {Fore.RED}wikipedia {Fore.WHITE}to go to Wikipedia.")
  print(spacer3+f"{Fore.WHITE}Type {Fore.RED}urban {Fore.WHITE}to go to Urban Dictionary.")
  print(spacer3+f"{Fore.WHITE}Type {Fore.RED}about {Fore.WHITE}to learn more.")
  print(spacer3+f"{Fore.WHITE}Type {Fore.RED}suggestion {Fore.WHITE}to give a suggestion.\n")

  print(spacer4+f"🔍 Search:")

  searchinput = input(f"{spacer3}{Fore.LIGHTYELLOW_EX}>{Fore.BLUE}>{Fore.RED}>{Fore.WHITE} ")

  clearpage()
  try:
    if searchinput == 'about':
      about()
    elif searchinput == "wikipedia":
      wiki()
    elif searchinput == "suggestion":
      suggestion()
    elif searchinput == "urban":
      urban()
    else:
      try:
        searchbar = f"{Fore.WHITE}{spacer2}({searchinput}{spacer4}|🔍)"
        print(logo)
        print(searchbar)
        s = searchinput.replace(" ", "+")
        for res in search(s, lang='en', num_results=50):
          print(f"{Fore.YELLOW}> {Fore.LIGHTBLUE_EX}{res}\n")
        conf = input(f"{spacer3}{Fore.WHITE}Want to Return?( ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
        if conf == 'y':
          home_page()
        elif conf == "n":
          home_page()
        else:
          return
      except:
        print(logo)
        print(searchbar)
        print(f"{Fore.RED} 404 Error")
        sleep(3)
        home_page()
  except:
    pass

def about():
  clearpage()
  print(abouts)

# About information
  type(f"{Fore.BLUE}\nF{Fore.RED}o{Fore.LIGHTYELLOW_EX}o{Fore.BLUE}g{Fore.LIGHTGREEN_EX}l{Fore.RED}e{Fore.WHITE} was created by {Fore.LIGHTGREEN_EX}Alex Tomsovic! (@AlexTomsovic){Fore.WHITE}\n")

# Features title
  print(f"{spacer1}{Fore.BLUE}F{Fore.RED}E{Fore.LIGHTYELLOW_EX}A{Fore.BLUE}T{Fore.LIGHTGREEN_EX}U{Fore.RED}R{Fore.BLUE}E{Fore.LIGHTYELLOW_EX}S{Fore.WHITE}\n")

# Features information
  sp(f"{Fore.RED}● {Fore.WHITE}Google Search\n{Fore.RED}● {Fore.WHITE}Urban Dictionary\n{Fore.RED}● {Fore.WHITE}Wikipedia\n{Fore.RED}● {Fore.WHITE}Suggestions\n{Fore.RED}● {Fore.WHITE}Encyclopedia Britannica {Fore.LIGHTYELLOW_EX}(Coming Soon)\n{Fore.RED}● {Fore.WHITE}CNN {Fore.LIGHTYELLOW_EX}(coming soon)\n")

# Socials title
  print(f"{spacer1}{Fore.BLUE}S{Fore.RED}O{Fore.LIGHTYELLOW_EX}C{Fore.BLUE}I{Fore.LIGHTGREEN_EX}A{Fore.RED}L{Fore.BLUE}S{Fore.WHITE}\n")

# Socials information
  sp(f"{Fore.RED}● {Fore.WHITE}Instagram: {Fore.LIGHTBLUE_EX} https://www.instagram.com/alexsdiabolicalworld/\n{Fore.RED}● {Fore.WHITE}YouTube: {Fore.LIGHTBLUE_EX} https://youtube.com/channel/UC8BGucwg0c0oTW6GwGJi_8Q/  \n{Fore.RED}● {Fore.WHITE}GitHub: {Fore.LIGHTBLUE_EX} https://github.com/alexandertomsovic/\n{Fore.RED}● {Fore.WHITE}LinkTree: {Fore.LIGHTBLUE_EX} https://linktr.ee/alextomsovic/\n")
  
  conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE})")
  if conf == 'y':
    home_page()
  else:
    return

# Searching Commands 
def searchoutput():
  clearpage()
  try:
    if searchinput == 'about':
      about()
    elif searchinput == "wikipedia":
      wiki()
    elif searchinput == "suggestion":
      suggestion()
    elif searchinput == "urban":
      urban()
    else:
      try:
        search_bar = f"{Fore.WHITE}{spacer2}({searchinput}{spacer4}|🔍)"
        print(logo)
        print(search_bar)
        s = searchinput.replace(" ", "+")
        for res in search(s, lang='en', num_results=50):
          print(f"{Fore.YELLOW}> {Fore.LIGHTBLUE_EX}{res}\n")
        conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
        if conf == 'y':
          home_page()
        elif conf == "n":
          home_page()
        else:
          return
      except:
        print(logo)
        print(search_bar)
        print(f"{Fore.RED} 404 ERROR")
        sleep(3)
        home_page()
  except:
    pass

# Wikipedia request
def wiki():
  clearpage()
  print(wiki_logo)
  print(spacer4+f"🔎 Search:")
  
  wikisearchq = input(f"{spacer3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")
  
  wikis = wikisearchq.replace(" ", "+")
  try:
    wikires = requests.get(f"https://allin1-api.glique.repl.co/wikipedia?word={wikis}&length=5").json()
    
    sum = wikires["result"]
    
    wiki_search_bar = f"{Fore.WHITE}{spacer2}({wikisearchq}{spacer4}|🌐)"
    
    clearpage()
    print(wiki_logo)
    print(wiki_search_bar)
    sp(f"{sum}\n")
    print(f"URL: {Fore.LIGHTBLUE_EX}https://en.wikipedia.org/wiki/{wikis}")
    conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      wiki()
    else:
      return
  except:
    wiki_search_bar = f"{Fore.WHITE}{spacer2}({wikisearchq}{spacer4}|🌐)"
    clearpage()
    print(wiki_logo)
    print(wiki_search_bar)
    print(f"{Fore.RED} . Found")
    conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      wiki()
    else:
      return

# Urban Dictionary request
def urban():
  clearpage()
  print(urban_logo)
  print(spacer4+f"🔎 Search:")
  
  udsearchq = input(f"{spacer3}{Fore.BLUE}>{Fore.LIGHTYELLOW_EX}>{Fore.RED}>{Fore.WHITE} ")
  ud_search_bar = f"{Fore.WHITE}{spacer2}({udsearchq}{spacer4}|📚)"
  uds = udsearchq.replace(" ", "%20")
  try:
    res = requests.get(f"https://udict-api.glique.repl.co/{uds}").json()
    auth = res["author"]
    defi = res["definition"]
    example = res["example"]
    url = res["permalink"]

    data = f"{Fore.RED}AUTHOR:\n{Fore.WHITE}{auth}\n\n{Fore.RED}DEFINITION:\n{Fore.WHITE}{defi}\n\n{Fore.RED}EXAMPLE:\n{Fore.WHITE}{example}\n\n{Fore.RED}URL: {Fore.LIGHTBLUE_EX}{url}"
    clearpage()
    print(urban_logo)
    print(ud_search_bar)
    sp(data)

    conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    elif conf == "n":
      urban()
    else:
      return
  except:
    ud_search_bar = f"{Fore.WHITE}{spacer2}({udsearchq}{spacer4}|📚)"
    clearpage()
    print(urban_logo)
    print(ud_search_bar)
    print(f"{Fore.RED} Not Found :(")
    conf = input(f"{spacer3}{Fore.WHITE}Want to Go Back? ({Fore.GREEN}y{Fore.WHITE}/{Fore.RED}n{Fore.WHITE}){Fore.WHITE} ")
    if conf == 'y':
      home_page()
    else:
      return

# Suggestion request
def suggestion():
  clearpage()
  print(suggestion_logo)
  name = input("Enter your social media platform and username(Discord, Twitter, Instagram) \n>>> ")
  title = input("Title of suggestion\n>>> ")
  desc = input("Suggestion body\n>>> ")
  weburl = os.getenv("weburl")
  
  # Client data
  data = {
    "username": "FOOGLE CLIENT",
    "content": "@everyone",
    "embeds": [{
      "author": {
        "name": name
      },
      "title": title,
      "description": desc
    }]
  }

  res = requests.post(weburl, json=data)

  print(f"Response Code: {res.status_code}\nDirecting you to the home page.")
  sleep(1)
  print("3")
  sleep(1)
  print("2")
  sleep(1)
  print("1")
  sleep(1)
  home_page()


# The Base
clearpage()
print(logo)
print(spacer3+f"{Fore.WHITE}Type {Fore.RED}wikipedia {Fore.WHITE}to go to Wikipedia.")
print(spacer3+f"{Fore.WHITE}Type {Fore.RED}urban {Fore.WHITE}to go to Urban Dictionary.")
print(spacer3+f"{Fore.WHITE}Type {Fore.RED}about {Fore.WHITE}to learn more.")
print(spacer3+f"{Fore.WHITE}Type {Fore.RED}suggestion {Fore.WHITE}to give a suggestion.\n")
print(spacer4+f"🔎 Search:")
searchinput = input(f"{spacer3}{Fore.LIGHTYELLOW_EX}>{Fore.BLUE}>{Fore.RED}>{Fore.WHITE} ")

searchoutput()
