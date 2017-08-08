#http://www.imdb.com/chart/top?ref_=nv_mv_250_6

import requests
from bs4 import BeautifulSoup

html_data = requests.get("http://www.imdb.com/chart/top?ref_=nv_mv_250_6").content

soup_data = BeautifulSoup(html_data, "html.parser")

tbody_data = soup_data.find("tbody", {"class":"lister-list"})

for tr_data in tbody_data.find_all("tr"):
    isim_td = tr_data.find("td",{"class":"titleColumn"})
    rating_td = tr_data.find("td", {"class":"ratingColumn"})
    print(isim_td.find("a")["href"])
    print(isim_td.find("a").text, rating_td.find("strong").text)
