import requests
import json
from bs4 import BeautifulSoup
file=open("moviedata.json")
movies=json.load(file)
def group_by_year():
    dic={}
    for i in movies:
        movie_list=[]
        year=i["year"]
        if year not in dic:
            for j in movies:
                if year==j["year"]:
                    movie_list.append(j)
            dic[year]=movie_list
    with open("movie.json","w+") as file1:
        json.dump(dic,file1,indent=4)
        b=json.dumps(dic)
group_by_year()
    
        




