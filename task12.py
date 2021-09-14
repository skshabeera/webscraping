import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/m/toy_story_4"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
def scrape_movie_cast(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    movie=soup.find("div",class_="castSection")
    main_div=movie.find("div",class_="media-body")
    div=main_div.find("a",class_="unstyled articleLink").get_text()
    print(div)
    
scrape_movie_cast(url)