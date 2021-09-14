import requests
import json
from bs4 import BeautifulSoup
with open("task5.json","r") as file:
    data1=json.load(file)
movie_data=data1
def analyse_language_and_directors(movie_list):
    dic={}
    for i in movie_list:
        for dirctor in i["Director"]:
            dic[dirctor]={}
    for i in range(len(movie_data)):
        for director in dic:
            if director in movie_data[i]["Director"]:
                for language in movie_data[i]["Language"]:
                    dic[director][language]=0
    for i in range(len(movie_data)):
        for director in dic:
            if director in movie_data[i]["Director"]:
                for language in movie_data[i]["Language"]:
                    dic[director][language]+=1
    with open("task10.json","w")as f:
        json.dump(dic,f,indent=4)
analyse_language_and_directors(movie_data)   