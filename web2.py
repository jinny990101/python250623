# web2.py

#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request

#페이징처리(0부터 9까지)
for i in range(0,10):
    #https://www.clien.net/service/board/sold?&od=T31&category=0&po=9
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "html.parser")
    list = soup.find_all("span", attrs={"data-role":"list-title-text"})
    print("페이지:", i+1)
    for tag in list:
        title = tag.text.strip()
        title = title.replace("\n", "")
        print("    ",title)
        f.write(title + "\n")
f.close()
        
