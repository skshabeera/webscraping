import requests
import os
from task1 import scrape_top_list
movie=scrape_top_list()
def get_movie_details_list():
    for i in movie:
        path="/home/dell49/Desktop/webscraping/movie.text"+i["moviename"]+"text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell49/Desktop/webscraping/movie.text"+i["moviename"]+".text","w")
            url=requests.get(i["url_add"])
            create1=create.write(url.text)
            create.close()
get_movie_details_list()





