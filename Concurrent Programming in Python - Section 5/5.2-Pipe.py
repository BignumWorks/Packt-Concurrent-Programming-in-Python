import multiprocessing
import random
import time

__author__ = "Mithun"

class Producer(multiprocessing.Process):
    def __init__(self, conn):
        multiprocessing.Process.__init__(self)
        self.conn = conn

    def run(self):
        for i in range(10):
            (x, y) = random.randint(1, 100000), random.randint(1, 100000)
            self.conn.send((x, y))
            print("Process {} added: {}".format(self.name, (x, y)))
        self.conn.close()

class Consumer(multiprocessing.Process):
    def __init__(self, conn):
        multiprocessing.Process.__init__(self)
        self.conn = recv

    def run(self):
        time.sleep(2)
        while True:
            try:
                (x, y) = self.conn.recv()
                print("Product of ({}*{}) = {}".format(x, y, x*y))
            except EOFError:
                print("No more data...")
                break

        self.conn.close()


if __name__ == "__main__":
    (recv, send) = multiprocessing.Pipe(False)

    p = Producer(send)
    p.start()


    send.close()

    c = Consumer(recv)
    c.start()

