from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.prettify())
all_movie_list = soup.find_all(name="h3", class_="title")
#print(all_movie_list)

movie_titles = [movie.getText() for movie in all_movie_list]

for movie in reversed(movie_titles):
    print(movie)

# print(movie_titles)