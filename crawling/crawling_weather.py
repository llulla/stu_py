from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=날씨'
html = requests.get(url)
#print(html.text)

soup = bs(html.text,'html.parser')
#pprint(soup)

data1 = soup.find('div',{'class':'report_card_wrap'}) #영역 추출
pprint(data1)

data2 = data1.findAll('item_today')
#pprint("data2 = ",data2[0])

find_dust = data2[0].find('span',{'class':'num'}).text
#pprint("find_dust = ",find_dust)

#finish