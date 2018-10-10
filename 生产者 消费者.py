import time
import threading
import random
from random import choice
import queue



def product(tasks,goods):
    while 1:

        task = choice(goods)
        time.sleep(random.randint(1,3))
        tasks.put(task)
        print('生产水果:{}'.format(task))

def consumer(tasks):
    while 1:
        time.sleep(random.randint(2,4))
        task = tasks.get()
        print('消费水果 ：{}'.format(task))
        print(tasks)




if __name__ == '__main__':
    tasks=queue.Queue(3)
    goods = ['栗子', '苹果', '香蕉', '橘子','西瓜','葡萄','梨子','山竹','桃子','无花果']
    t1 = threading.Thread(target=product,args=(tasks,goods))
    t2 = threading.Thread(target=consumer,args=(tasks,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


