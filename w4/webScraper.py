import requests
from bs4 import BeautifulSoup

def scrape_web(url):
    for i in range(3):
        print('---------------')
        try:
            get_url_info = requests.get(url)
        except:
            print('{}はアクセスできひん...'.format(url))
            print()
            return

        soup = BeautifulSoup(get_url_info.content, 'lxml')
        url_list = []

        try:
            print(soup.title.string)
        except:
            pass
        print('({})'.format(url))
        print('---------------')

        # TODO: metaタグのcontentにも対応させる
        for a_tag_list in soup.find_all('a'):
            if not a_tag_list:
                break
            href_path = a_tag_list.get('href')
            if href_path is None:
                continue
            if href_path.startswith(('https://', 'http://')) and not href_path in url_list:
                url_list.append(href_path)
                print(href_path)

        print()
        return url_list


def loop_scrape(url_list):
    len_url_list = len(url_list)
    second_url_list = [[] for i in range(len_url_list)]
    for i in range(len_url_list):
        second_url_list.append(scrape_web(url_list[i]))
    return second_url_list

def double_loop_scrape(second_url_list):
    for i in range(len(second_url_list)):
        for j in range(len(second_url_list[i])):
            scrape_web(second_url_list[i][j])


# NOTE: def main
input_url = input('URL入力してな: ')

print('---1---')
input_url_list = scrape_web(input_url)
print('---2---')
second_url_list = loop_scrape(input_url_list)

third_url_show = input('3層目のURLリストアップする？ y/n: ')
if third_url_show in {'y', 'yes'}:
    print('---3---')
    double_loop_scrape(second_url_list)
