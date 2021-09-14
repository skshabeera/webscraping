import requests
import json
from bs4 import BeautifulSoup
with open("task5.json","r+") as file:
    b=json.load(file)
def analyse_movies_language(b):
    dic={}
    for i in b:
        if "Language" in i:
            Language=i["Language"]
            for i in Language:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
    with open("task6.json","w+") as file:
        json.dump(dic,file,indent=6)
    return dic

analyse_movies_language(b)