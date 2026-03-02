import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/AI_Art/index.html"
headers_dic = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
#
response = requests.get(url, headers=headers_dic)
#analyze the webpage content
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_="r-ent")
#print the {title} and {popularity} of each article
for article in articles:
    title = article.find('div', class_='title')
    if title.a and title:
        title = title.a.text
    else:
        title = "本文已被刪除"
    print(title)
    popular = article.find('div', class_='nrec')
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "0"
    print(f"Popularity: {popular}")