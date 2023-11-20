import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch

speak=Dispatch("SAPI.SpVoice")
# speak.speak(i)

r=requests.get("https://www.geo.tv/category/pakistan")
# # print(r)
# # print(r.text)
soup=BeautifulSoup(r.text,"lxml")
div=soup.findAll('div' , attrs={"class":"entry-title"} , limit=10) #i extracted only 

print("********** Starting to read news **********")
for i in range(1,10):
    speak.speak(div[i].h2.text)
    

print("********** Thank you for your attention! **********")
input("<====Press enter to exit====>")
# news_list=[(div[i].h2.text) for i in range(1,10) ]
# print(news_list)