import requests
url = "https://www.ptt.cc/bbs/AI_Art/index.html"
headers_dic = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers_dic)
#print(response.text) 
if response.status_code == 200:
    # 將網頁內容寫入本地檔案 
    with open("1st_try.html", "w", encoding="utf-8") as file:  
        file.write(response.text)
    print("write successful")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
