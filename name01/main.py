__author__ = 'Tang Daye'

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.sina.com.cn/china/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, "html.parser")
newsList = soup.select(".news-item")
print([news.text for news in newsList])

