import time
import random
import json
import requests
with open("task5.json","r+")as f:
    d=json.load(f)
m=d
def get_movies(m):
    for i in m:
        random_sleep=random.randint(1,3)
        path=open("/home/dell49/Desktop/webscraping/text.txt"+i["movie_name"]+"text","w+")
        d=str(i)
        creaer=path.write(d)
        time.sleep(random_sleep)
        path.close()
get_movies(m)
