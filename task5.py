import requests
import json
from task1 import scrape_top_list
from task4 import movies_detailes
movie=scrape_top_list()
moviedata=movie[:100]
def get_movie_detailes():
    list=[]
    for i in moviedata:
        for j in i:
            if j=="url_add":
                
                list.append(movies_detailes(i[j]))
    with open("task5.json","w") as file:
        json.dump(list,file,indent=4)
    return list
get_movie_detailes()