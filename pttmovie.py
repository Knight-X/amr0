import re
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.ptt.cc/bbs/movie/index.html')

soup = BeautifulSoup(res.text, "html.parser")

index = soup.find_all(text=re.compile("上頁"), class_ = 'btn wide')
tmp = str(index[0]['href'])
var = re.search(r'[0-9]+', tmp) 
print(var.group())

for x in range (3810, int(var.group())):
    target_url = 'https://www.ptt.cc/bbs/movie/index' + str(x) + '.html'

    res_dst = requests.get(target_url)

    soup_dst = BeautifulSoup(res_dst.text, "html.parser")
    print(target_url)
    for entry in soup_dst.find_all("div", class_ = "title"):
        if entry.a is not None:
            print(entry.a.text)




