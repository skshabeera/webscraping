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
    return dic
dec=group_by_year()
def group_by_decade(movies):
    movie_dict={}
    list1=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movie_dict[i]=[]
    for i in movie_dict:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    movie_dict[i].append(v)
    # print(movie_dict)
    with open("task3.json","w+") as file:
        json.dump(movie_dict,file,indent=4)
        b=json.dumps(movie_dict)

group_by_decade(dec)

    