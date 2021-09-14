import json,requests
from task1 import scrape_top_list
movies=scrape_top_list()
with open("task5.json","r+")as f:
    movies_detailes=json.load(f)
data=movies_detailes    
def analyse_language_and_directors(movies_list):
    dic={}
    for i in movies_list:
        for director in i["Director"]:
            dic[director]={}   
    for j in range(len(movies_list)):
        for director in dic:
            if director in movies_list[j]["Director"]:
                for language in movies_detailes[j]["Language"]:
                    print(language)
                    # dic[director][language]=0
    # print(dic)                 
analyse_language_and_directors(data)        