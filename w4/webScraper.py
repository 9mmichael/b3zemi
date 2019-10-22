import requests
from bs4 import BeautifulSoup
# import os

def scrape_web(url):
    for i in range(3):
        print('---------------')
        try:
            get_url_info = requests.get(url)
        except:
            print('{}はアクセスできひん...'.format(url))
            print()
            return

        soup = BeautifulSoup(get_url_info.text, 'lxml')
        url_list = []

        # FIXME: titleタグあるのに文字化け(?)してしまう
        print(soup.title.string)
        print('({})'.format(url))
        print('---------------')

        # TODO: metaタグのcontentにも対応させる
        for a_tag_list in soup.find_all('a'):
            if not a_tag_list:
                break
            href_path = a_tag_list.get('href')
            if href_path is None:
                continue
            if href_path.startswith('http://'):
                url_list.append(href_path)
                print(href_path)

        print()
        return url_list


def loop_scrape(url_list):
    for i in range(len(url_list)):
        scrape_web(url_list[i])

input_url = input('URL入力してな: ')

# TODO: 何層スクレイピングするかの指定
"""
loop_count = input('何層スクレイピングする？: ')
if not type(loop_count is int):
    print('int型でよろしゅう')
    sys.exit(status=None)
loop_count = int(loop_count)
if loop_count < 1:
    print('1層以上でよろしゅう')
    sys.exit(status=None)
if loop_count > 5:
    print('5層以上はきついで...')
    sys.exit(status=None)
"""

print('---1---')
input_url_list = scrape_web(input_url)
print('---2---')
loop_scrape(input_url_list)
