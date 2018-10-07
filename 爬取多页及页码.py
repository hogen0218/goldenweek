import requests
from bs4 import BeautifulSoup
import threading


list1 = []
title_list=[]
index_list = []
def start():
    url = 'http://blog.jobbole.com/all-posts/'
    list1.append(url)
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    list_title = soup.select('a.archive-title')
    list_index = soup.select('a.page-numbers')

    parse_index(list_index)


def get_html(url):
    r = requests.get(url)
    return r.text

def parse_title(list_title):
    for i in list_title:
        href = i.attrs['href']
        res = get_html(href)
        print(res)

def parse_index(list_index):
    global list1
    for i in list_index:
        href = i.attrs['href']
        if href in list1:
            continue
        list1.append(href)
        html = get_html(href)
        index_soup = BeautifulSoup(html,'lxml')
        next_list_title = index_soup.select('a.archive-title')
        threading.Thread(target=parse_title,args=(next_list_title,)).start()

        next_list_index = index_soup.select('a.page-numbers')
        parse_index(next_list_index)



if __name__ == '__main__':
    start()
    print(list1)