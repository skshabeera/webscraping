import requests
import json
from bs4 import BeautifulSoup
with open("task5.json","r") as file:
    a=json.load(file)
def analyse_movie_directors():
    dict={}
    for i in a:
        b=i["Director"]
        for j in b:
            if j not in dict:
                b=j
                dict[j]=1
            else:
                dict[j]+=1          
    with open("task7.json","w+") as file:
        json.dump(dict,file,indent=4)
analyse_movie_directors()
