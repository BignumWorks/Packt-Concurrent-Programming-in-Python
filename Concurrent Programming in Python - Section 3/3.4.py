import threading
import random
import time
import queue

__author__ = "Mithun"

q = queue.Queue()


class Producer(threading.Thread):
    def run(self):
        for i in range(10):
            (x, y) = random.randint(1, 100000), random.randint(1, 100000)
            q.put((x, y))
            print("Thread {} added: {}".format(self.name, (x, y)))
            time.sleep(random.random())


class Consumer(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(random.random())
            (x, y) = q.get()
            print("Product of ({}*{}) = {}".format(x, y, x * y))
            q.task_done()


Producer().start()
Consumer().start()

q.join()
