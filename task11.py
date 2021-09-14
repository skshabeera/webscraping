# import requests
import json 
# from bs4 import BeautifulSoup
with open("task5.json","r") as file:
    f=json.load(file)
def analyse_movie_genre(f):
    b=[]
    for i in f:
        if "Genre" in i:
            g=i["Genre"]
            b.append(g)
    l1=[]
    for i in b:
        if type([i])==list:
            for j in i:
                l1.append(j)
    l2=[]
    for i in l1:
        str=""
        for j in i:
            if j==",":
                pass
            else:
                str+=j
        l2.append(str)
    l3=[]
    for j in l2:
        if j not in l3:
            l3.append(j)
    l4=[]
    for i in l3:
        if i=="&":
            pass
        else:
            l4.append(i)
    # print(l4)
    dic={}
    for i in l4:
        c=0
        for j in l2:
            if i==j:
                c+=1 
        dic[i]=c
    print(dic)   
            
    with open("task11.json","w") as f1:
        json.dump(dic,f1,indent=4)   
analyse_movie_genre(f)
