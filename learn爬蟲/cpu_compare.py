import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/C_Chat/M.1768523504.A.621.html"
headers_dic = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36","Cookie":"over18=1"}
response = requests.get(url,headers = headers_dic)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)