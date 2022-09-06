from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/filmosearch/?explore=title_type&role=nm0000138&ref_=filmo_ref_typ&sort=release_date,desc&mode=detail&page=1&job_type=actor&title_type=movie"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
movies = soup.find_all('h3', class_="lister-item-header")
ans = []
for movie in movies:
    movie = movie.get_text().replace("\n", '')
    ans.append(movie)
for i in ans:
    print(i)