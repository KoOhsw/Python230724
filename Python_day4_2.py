#Web웹 - 당근 마켓
import os
import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('div', attrs={'class': 'card-desc'})

# 맥OS와 윈도우에서 모두 동작하도록 파일 경로 설정
file_path = os.path.join(os.getcwd(), 'daangn.txt')

with open(file_path, 'wt', encoding='utf-8') as f:
    for post in posts:
        title = post.find('h2', attrs={'class': 'card-title'})
        price = post.find('div', attrs={'class': 'card-price'})
        addr = post.find('div', attrs={'class': 'card-region-name'})

        title = title.text.replace('\n', '')
        price = price.text.replace('\n', '')
        addr = addr.text.replace('\n', '')

        print(f'{title},{price},{addr}')
        f.write(f'{title},{price},{addr}\n')
