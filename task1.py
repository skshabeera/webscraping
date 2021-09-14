import requests
import json
from bs4 import BeautifulSoup
url='https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
def scrape_top_list():
    list=[]
    mainDiv=soup.find("div",class_="panel-body content_body allow-overflow")
    subDiv=mainDiv.find("table",class_="table")
    alltrs=subDiv.find_all('tr')
    position=0
    for i in alltrs:
        dict={}
        alltds=i.find_all('td')
        for j in alltds:
            moviename=i.find("a",class_="unstyled articleLink")["href"][3::]
            rating=i.find('span',class_="tMeterIcon tiny").text[3:-2]
            review=i.find(class_="right hidden-xs").get_text()[-4:-1]
            year=i.find("a",class_="unstyled articleLink").text[-5:-1]
            url_add="https://www.rottentomatoes.com/m/"+moviename
            dict["position"]=position
            dict["moviename"]=str(moviename)
            dict["rating"]=float(rating)
            dict["review"]=int(review)
            dict["year"]=int(year)
            dict["url_add"]=str(url_add)
            dict["position"]=position
            if dict not in list:
                position+=1
                list.append(dict)
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
    # position=+1
scrape_top_list()

