import urllib3
from threading import Thread

import time
import random

urllib3.disable_warnings()

__author__ = "Mithun"


class URLDownload(Thread):
    def __init__(self, url_name, url):
        Thread.__init__(self)
        self.url = url
        self.url_name = url_name

    def run(self):
        time.sleep(random.random())

        print("Thread {} : URL: {}, URLName: {}. \r\n".format(self.name, self.url, self.url_name))


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
