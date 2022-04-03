#!./bin/python3
import pandas
import requests
from bs4 import BeautifulSoup



def load_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    response = requests.get(url ,headers=headers)

    content = response.content
    return BeautifulSoup(content,"html.parser")


def extract_url(soup):
    link_set = set()
    final_list =  []
    links = soup.find_all("a")
    for link in links:
        href = link.get('href')
        if href and not href.startswith('/wiki'):
            link_set.add(href)
        elif href and href.endswith('/wiki/'):
            continue
        elif href:
            link_set.add('https://en.wikipedia.org' + href)

    return link_set





soup = load_soup("https://en.wikipedia.org/wiki/Main_Page")

link_set = extract_url(soup)

print(pandas.DataFrame([ link_s for link_s in link_set if not link_s.endswith('/wiki/') and link_s.startswith('https') ]).to_csv())
