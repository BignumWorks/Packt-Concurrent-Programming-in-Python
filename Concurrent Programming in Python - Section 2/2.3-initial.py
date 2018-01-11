import urllib3
from threading import Thread

urllib3.disable_warnings()

__author__ = "Mithun"


class URLDownload(Thread):
    def __init__(self, file_name, url):
        Thread.__init__(self)
        self.file_name = "Thread_" + file_name
        self.url = url

    def run(self):
        print("Downloading the contents of {} into {}".format(self.url, self.file_name))
        http = urllib3.PoolManager()

        response = http.request(method="GET", url=self.url)
        with open(self.file_name, "wb") as f:
            f.write(response.data)

        print("Download of {} done".format(self.url))


threads = []
test_dict = {
    "Google": "http://www.google.com",
    "Python": "http://www.python.org",
    "Bing": "http://www.bing.com",
    "Yahoo": "http://www.yahoo.com"
}

print("Main thread starting execution...")
for key in test_dict:
    thread = URLDownload(key, test_dict[key])
    threads.append(thread)
    thread.start()

print("Main thread continuing execution...")
for thread in threads:
    thread.join()

print("Main thread exiting...")
