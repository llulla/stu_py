from bs4 import BeautifulSoup
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

data1=soup.findAll('a',{'class':'title'})
week_title_list=[t.text for t in data1]
print(week_title_list)

# # 모든요일 웹툰영역 추출
# data1_list = soup.findAll('div',{'class':'col_inner'})
# print(len(data1_list))

# #전체 웹툰 리스트
# week_title_list = []

# for data1 in data1_list:
#     #제목 포함영역 추출
#     data2=data1.findAll('a',{'class':'title'})
#     #텍스트만 추출
#     title_list= [t.text for t in data2]
#     week_title_list.append(title_list)
    #week_title_list.extend(title_list)

#    print(title_list)


# data2=data1.findAll('a',{'class':'title'})
# print(data2)

#title_list=[]
#for t in data2:
#    title_list.append(t.text)

# mon_title_list=[t.text for t in data2]

# print(mon_title_list)


#finish