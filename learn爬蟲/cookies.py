import requests
from bs4 import BeautifulSoup
import os
def download_image(url, save_path):
    print(f"Downloading image from {url} to {save_path}")
    respnse = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(respnse.content)
    print("-"*30)
def main():
    url = "https://www.ptt.cc/bbs/C_Chat/M.1768523504.A.621.html"
    headers_dic = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36","Cookie":"over18=1"}
    response = requests.get(url,headers = headers_dic)
    soup = BeautifulSoup(response.text, 'html.parser')
    spans = soup.find_all('span', class_="article-meta-value")
    title = spans[2].text
    # Create directory named after the title
    dir_name = f"{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    #find all image tags
    links = soup.find_all('a')
    allow_file_types = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    for link in links:
        href = link.get('href')
        if not href:
                continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        if extension  in allow_file_types:
            print(f"file type: {extension}")
            print(f"Downloading image: {href}")
            download_image(href, f"{dir_name}/{file_name}")
if __name__ == "__main__":
    main()