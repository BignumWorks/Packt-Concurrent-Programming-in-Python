from threading import Thread, RLock

import time
import random

print_lock = RLock()
class URLDownload(Thread):

    def __init__(self, urlName, url):
        Thread.__init__(self)
        self.url = url
        self.urlName = urlName

    def run(self):
        time.sleep(random.random())
        print_lock.acquire()
        print_lock.acquire()
        print("Thread {} : URL: {}, URLName: {}. \r\n".format(self.name, self.url, self.urlName))
        print_lock.release()
        print_lock.release()


threads = []
test_dict = {
    "Google": "http://www.google.com",
    "Python": "http://www.python.org",
    "Bing": "http://www.bing.com",
    "Yahoo": "http://www.yahoo.com",
    "Amazon": "http://www.amazon.com",
    "Nike": "http://www.nike.com",
    "Wikipedia": "https://www.wikipedia.com"
}

for key in test_dict:
    for i in range(10):
        thread = URLDownload(key, test_dict[key])
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
