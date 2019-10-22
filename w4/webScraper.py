import requests
from bs4 import BeautifulSoup
import os
import re

# status_code = get_url_info.status_code

# print(status_code)

# if not (status_code == 200):
# sys.exit(status=None)
# get_url_info = requests.get('https://qiita.com/__init__/items/d53a281ef757b22f4732')
# get_url_info.raise_for_status()

def scrape_web(url):
    get_url_info = requests.get(url)
    # FIXME: 読み込めなかった時にexitされないようにする

    soup = BeautifulSoup(get_url_info.text, 'lxml')
    url_list = [] * 1

    for a in soup.find_all('a'):
        href_path = a.get('href')
        if href_path.startswith('http://'):
            url_list.append(href_path)

    return url_list


ans = scrape_web("https://qiita.com/__init__/items/d53a281ef757b22f4732")
print(ans)

ans2 = scrape_web(ans[0])
print(ans2)

for i in range(len(ans)):
    tmp_ans = scrape_web(ans[i])
    print(tmp_ans)
