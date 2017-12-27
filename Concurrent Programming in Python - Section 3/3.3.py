import threading
import random
import time

operands = []
event = threading.Event()

class Producer(threading.Thread):
    def run(self):
        while True:
            (x, y) = random.randint(1, 100000), random.randint(1, 100000)
            operands.append((x, y))
            print("Thread {} added: {}".format(self.name, (x, y)))
            event.set()
            time.sleep(random.random())

class Consumer(threading.Thread):
    def run(self):
        while True:
            time.sleep(random.random())
            event.wait()
            (x, y) = operands.pop()
            print("Product of ({}*{}) = {}".format(x, y, x*y))
            event.clear()

Producer().start()
Consumer().start()
