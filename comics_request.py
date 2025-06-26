import requests
import json
import os
from PyQt6.QtGui import QPixmap
from bs4 import BeautifulSoup



headers = {
        
        "referer" : "https://comic.naver.com/webtoon?tab=mon",
        "sec-ch-ua" : '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
    }

def re1(url):

    response = requests.get(url=url, headers=headers)
    response = json.loads(response.text)
    
    titles = {name['titleName'] : (name['titleId'], name['thumbnailUrl']) for name in response['titleList']}
    
    
    return titles


#titles = re("https://comic.naver.com/api/webtoon/titlelist/weekday?week=mon")
#print(titles)

def re2(url):
    
    response = requests.get(url=url, headers=headers)
    
    try:
        
        if response.status_code == 200:
            
            pixmap = QPixmap()
            
            if pixmap.loadFromData(response.content):
                
                return pixmap
        
        else:   print(f"status code error : {response.status_code}")
        
        return pixmap
    
    except Exception as e:    print(f"error : {e}")
    

def re3(url):
    
    response = requests.get(url=url, headers=headers)
    response = json.loads(response.content)
    
    response = response['articleList'][0]['no']
    
    return response
    

#count = re3("https://comic.naver.com/api/article/list?titleId=821597&page=1")
#print(count)

def re4(url, no):
    
    response = requests.get(url=url, headers=headers)
    response = json.loads(response.content)
    response = response['articleList']
    
    for c in response:
        
        if c['no'] == no:
            
            return (c['thumbnailUrl'], c['subtitle'])
    

#thum = re4("https://comic.naver.com/api/article/list?titleId=821597&page=2", 48)
#print(thum)


def re5(url):

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    soup = soup.find('div', attrs={'class': 'wt_viewer'})
    soup = soup.find_all("img")
    
    links = []
    
    for link in soup:
        
        link = link["src"]
        
        links.append(link)
        
    return links


def re6(url, comic_num, no, path):
    
    path = create_folder(path, comic_num, no)
    
    headers = {
        
        "referer" : f"https://comic.naver.com/webtoon/detail?titleId={comic_num}&no={no}",
        "sec-ch-ua" : '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
    }
    
    response = requests.get(url=url, headers=headers)
    
    name = url.split('_')[-1]
    
    if response.status_code == 200:
        
        with open(f"{path}\{name}", "wb") as f:
            
            f.write(response.content)
            
    else:
        
        print(f"요청 실패: {response.status_code}")
        
def create_folder(path, comic_num, no):
    
    path = f"{path}\\{comic_num}\\{no}"
    
    os.makedirs(path, exist_ok=True)

    return path


