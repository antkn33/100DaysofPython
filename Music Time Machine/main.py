#
from bs4 import BeautifulSoup
import requests

# date = "1987-06-01"
date = input("Select a date to view the Hot 100 Chart in this format: YYYY-MM-DD. ")

url = "https://www.billboard.com/charts/hot-100/" + date

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=headers)

chart = response.text

soup = BeautifulSoup(chart, "html.parser")
# (print(soup.prettify()))

song_list = soup.select("li ul li h3")

# print(song_list)

song_title = [title.getText().strip() for title in song_list]

number = 0
for song in song_title:
    number += 1
    print(str(number) + " " + song)