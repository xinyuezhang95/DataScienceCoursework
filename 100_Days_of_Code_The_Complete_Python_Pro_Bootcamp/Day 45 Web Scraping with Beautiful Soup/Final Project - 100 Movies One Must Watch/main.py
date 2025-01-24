import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_web_page = response.text

# print(movies_web_page)

soup = BeautifulSoup(movies_web_page, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name = "h3", class_ = "title")
# print(all_movies)

movie_titles = [movie.get_text() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode = "w", encoding = "utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")