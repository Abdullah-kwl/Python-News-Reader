import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch

speak=Dispatch("SAPI.SpVoice")
# speak.speak("Hello world")

r=requests.get("https://www.geo.tv/category/pakistan")
soup=BeautifulSoup(r.text,"lxml")

print()
print("********** We have top 50 news headlines **********")
a=int(input("How many news headlines you want to know ? : "))
while a<1 or a>50:
    print()
    print("please enter corretaly  !")
    print("please enter number between 1 to 50 !")
    a=int(input("How many news headlines you want to know ? : "))



div=soup.findAll("h2", limit=(a+1)) #i extracted only 
for news in div:
    print()
    print(news.text)
    speak.speak(news.text)

print()
print("********** Tnanks for your's attention **********")
input("<============= press enter to exit ==============>")