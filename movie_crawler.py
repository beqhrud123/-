#student_1
import requests
from bs4 import BeautifulSoup as bs
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220530'
data = requests.get(url)
soup = bs(data.text)

meta = soup.find_all('meta')

IstRanking = soup.find("table",{"class":"list_ranking"})

div = IstRanking.find('div',{'class':'tit5'})
title = div.find('a')['title']
point = IstRanking.find('td',{'class':'point'})
acClass = IstRanking.find('td',{'class':'ac'})
rank = acClass.find('img')['alt']
print('<<현재 상영중인 영화 랭킹>>')
print(rank, title, point.text)

trTag = IstRanking.findAll('tr')
for Li in trTag[:33]:
        try:
           info = Li.find("div", {"class": 'tit5'})
           aTag = info.find('a')
           title = aTag['title']

           acCLass = Li.find('td',{'class':'ac'})
           rank = acCLass.find('img')['alt']

           point = Li.find('td',{'class':'point'})
           point = point.text

           print(rank, title, point)
        except Exception as e:
           print('---------------')
#return {'rank':rank, 'title':title, 'point':point}

#student2

import bs4
import requests
from bs4 import BeautifulSoup
import csv

need_reviews_cnt = 100
reviews = []
review_data=[]

for page in range(1,50):
    url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    reviews = soup.find_all("td",{"class":"title"})
    
    for review in reviews:
        sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
        if sentence != "":
            movie = review.find("a",{"class":"movie color_b"}).get_text()
            score = review.find("em").get_text()
            review_data.append([movie,sentence,int(score)])
            need_reviews_cnt-= 1     
    if need_reviews_cnt < 0:                                         
        break

columns_name = ["movie","sentence","score"]
with open ( "samples.csv", "w", newline ="",encoding = 'utf8' ) as f:
    write = csv.writer(f)
    write.writerow(columns_name)
    write.writerows(review_data)
