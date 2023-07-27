#Web웹 - 당근 마켓

# 웹통신
import requests
# 크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('div', attrs={'class':'card-desc'})

f = open('c:\\work\\daangn.txt','wt',encoding='utf-8')
for post in posts:
    title = post.find('h2', attrs = {'class':'card-title'})
    price = post.find('div', attrs = {'class':'card-price'})
    addr = post.find('div', attrs = {'class':'card-region-name'})

    title =title.text.replace('\n','')
    price =price.text.replace('\n','')
    addr =addr.text.replace('\n','')

    print(f'{title},{price},{addr}')
    f.write(f'{title},{price},{addr}\n')
f.close()
