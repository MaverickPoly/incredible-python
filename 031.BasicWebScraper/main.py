import requests
from bs4 import BeautifulSoup


# Web Scraper that scrapes quotes from a website
URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

with open("index.html", "w") as file:
    file.write(response.text)

bs = BeautifulSoup(response.text, "lxml")
quotes = [(el.find('span', class_="text").text[1:-1], el.find("small", class_="author").text)
          for el in bs.find_all("div", class_="quote")]

for quote, author in quotes:
    print(f"{quote} - {author}")
