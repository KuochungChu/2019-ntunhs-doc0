import requests
from lxml import html
import pandas
from bs4 import BeautifulSoup

# Note trailing backslash removed
url = "http://www.cnbc.com"
response = requests.get(url)
doc = html.fromstring(response.text)

headlineNode = doc.xpath('//a[@class="HeroLedePlusThreeDeckItem-thumbnailContainer"]')
print(len(headlineNode))

result_list  = []
for node in headlineNode:
    url_node = node.xpath('@href')
    title = node.xpath('@title')
    news_html = requests.get(url_node[0])
    soup = BeautifulSoup(news_html.content,'lxml')
    text =[''.join(s.findAll(text=True)) for s in soup.findAll("div", {"class":"group"})]
    if (url_node and title and text) :
        result_list.append({'URL' : url_node[0].strip(),
                            'TITLE' : title[0].strip(),
                            'TEXT' : text[0].strip()})

with open('/root/python/key-points.txt', 'w') as f:
    for item in result_list:
        f.write("%s\n" % item)