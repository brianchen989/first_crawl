import requests
from bs4 import BeautifulSoup
import json
url = "https://www.ptt.cc/bbs/AI_Art/index.html"
headers_dic = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
#get the webpage content
response = requests.get(url, headers=headers_dic)
#analyze the webpage content
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('div', class_="r-ent")
data_list = []
#print the {title} and {popularity} of each article
for article in articles:
    data = {}
    title = article.find('div', class_='title')
    if title.a and title:
        title = title.a.text
    else:
        title = "本文已被刪除"
    data['title'] = title
    popular = article.find('div', class_='nrec')
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "0"
    data['popularity'] = popular
    data_list.append(data)
print(data_list)
'''這是 Python 內建 json 模組的方法，用來把資料「倒進」檔案裡。括號內的參數非常關鍵：

data_list：這是你要儲存的資料（來源）。通常是一個包含很多標題、時間的列表（List）。

json_file：這是你要寫入的目標檔案（目的地）。

ensure_ascii=False：這非常重要！ 預設情況下，JSON 會把中文轉換成 ASCII 碼。設定為 False 才能讓檔案直接顯示人類看得懂的繁體中文。

indent=4：這是「縮排」。設定為 4，存出來的 JSON 檔案就會有漂亮的換行與空格（像階梯一樣），而不是擠成一團的長字串，方便人類閱讀。'''
with open("ptt_output.json", "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)
