'''
python CricInfoHeadlinesScraper.py > headlines.txt
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

urls = []
html = urlopen("http://www.espncricinfo.com/")
bsObj = BeautifulSoup(html.read())

for section in bsObj.find("section",{"class":"col-three"}):
    for link in section.find_all('a',{"name":re.compile("&lpos=cricket:feed:16:coll:headlines:\\d")}):
        urls.append('http://espncricinfo.com/'+link.attrs['href'])

#print(urls)

for url in urls:
    detailsHtml=urlopen(url)
    newbsObj=BeautifulSoup(detailsHtml.read())

    print(newbsObj.find('header',{'class':'article-header'}).text)
    print("\n")

    for paragraph in newbsObj.find("section",{"id":"article-feed"}).find_all("article",{"class":"article"})[0].find_all('p'):
        print(paragraph.text)
    print('-----------------------------------------------------------------\n\n')

