import requests
from bs4 import BeautifulSoup

def scrape_web(url):
    print('---------------')
    try:
        get_url_info = requests.get(url)
    except:
        print('{}はアクセスできん...'.format(url))
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

    for a_tag_list in soup.find_all('a'):
        if not a_tag_list:
            break
        href_elem = a_tag_list.get('href')
        if href_elem is None:
            continue
        if href_elem.startswith(('http://', 'https://')) and not href_elem in url_list:
            url_list.append(href_elem)
            print(href_elem)

    for meta_tag_list in soup.find_all('meta'):
        if not meta_tag_list:
            break
        content_elem = meta_tag_list.get('content')
        if content_elem is None:
            continue
        if content_elem.startswith(('http://', 'https://')) and not content_elem in url_list:
            url_list.append(content_elem)
            print(content_elem)

    print()
    return url_list


def single_loop_scrape(url_list):
    len_url_list = len(url_list)
    second_url_list = [[]]
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
second_url_show = input('2層目のURLリストアップする？ y/n: ')

if second_url_show in {'y', 'yes'}:
    print('---2---')
    second_url_list = single_loop_scrape(input_url_list)

third_url_show = input('3層目のURLリストアップする？ y/n: ')
if third_url_show in {'y', 'yes'}:
    print('---3---')
    double_loop_scrape(second_url_list)
