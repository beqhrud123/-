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
