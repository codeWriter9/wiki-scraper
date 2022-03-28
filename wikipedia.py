#!./bin/python3
import pandas
import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://en.wikipedia.org/wiki/Main_Page",headers=headers)


content = response.content
soup = BeautifulSoup(content,"html.parser")

#print(soup)

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

print(pandas.DataFrame([ link_s for link_s in link_set if not link_s.endswith('/wiki/') and link_s.startswith('https') ]).to_csv())
