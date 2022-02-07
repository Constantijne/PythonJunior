import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    r = requests.get("https://rezka.ag/films/western/page/1/")
    html = BS(r.content, 'html.parser')
    items = html.select(".b-content__inline > .b-content__inline_items")

    if len(items):
        for el in items:
            title = el.select('.b-content__inline_item > a')
            print(title[0].text)
        page += 1
    else:
        break
