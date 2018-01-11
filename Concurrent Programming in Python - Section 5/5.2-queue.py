import multiprocessing
import random
import time

__author__ = "Mithun"


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            time.sleep(random.random())
            (x, y) = random.randint(1, 100000), random.randint(1, 100000)
            self.queue.put((x, y))
            print("Process {} added: {}".format(self.name, (x, y)))


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        time.sleep(2)
        while not self.queue.empty():
            time.sleep(random.random())
            (x, y) = self.queue.get()
            print("Product of ({}*{}) = {}".format(x, y, x * y))

        self.queue.close()


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p = Producer(queue)
    p.start()

    c = Consumer(queue)
    c.start()

    p.join()
    c.join()
