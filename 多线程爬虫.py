import requests
from bs4 import BeautifulSoup
import threading
import queue
list1=[]
lock = threading.RLock()
def get_html(url):
    r = requests.get(url)
    return r.content.decode('utf8')

def detail(detail_tasks):
    while 1:
        temp = detail_tasks.get()
        temp_html = get_html(temp)
        print(temp_html)

def parse(detail_tasks,index_tasks):
    while 1:
        url = index_tasks.get()
        html = get_html(url)
        soup = BeautifulSoup(html,'lxml')
        details=soup.select('[class=post-thumb] a')

        for i in details:
            temp_url_detail=i['href']
            detail_tasks.put(temp_url_detail)

        indexs = soup.select('a[class=page-numbers]')
        for k in indexs:
            temp_url_index=k['href']
            if temp_url_index not in list1:
                lock.acquire()
                list1.append(temp_url_index)
                lock.release()
                index_tasks.put(temp_url_index)
            else:
                continue
if __name__ == "__main__":
    index_tasks = queue.Queue()
    detail_tasks=queue.Queue()
    url= 'http://blog.jobbole.com/all-posts/'
    index_tasks.put(url)
    t1 = threading.Thread(target=detail,args=(detail_tasks,))
    l = [threading.Thread(target=parse,args=(detail_tasks,index_tasks)) for i in range(20)]
    t1.start()
    for i in l:
        i.start()
    t1.join()
    for i in l:
        i.join()
