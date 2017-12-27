import urllib3
import threading
urllib3.disable_warnings()

__author__ = "Mithun"


def download_url(file_name, url):
    print("Downloading the contents of {} into {} in thread {}".format(url, file_name, threading.current_thread().name))
    http = urllib3.PoolManager()

    response = http.request(method="GET", url=url)
    with open(file_name, "wb") as f:
        f.write(response.data)

    print("Download of {} done".format(url))


threads = []
test_dict = {
    "Google": "http://www.google.com",
    "Python": "http://www.python.org",
    "Bing": "http://www.bing.com",
    "Yahoo": "http://www.yahoo.com"
}

print("Main thread starting execution...")
for key in test_dict:
    thread = threading.Thread(target=download_url, name=key, args=(key, test_dict[key]))
    threads.append(thread)
    thread.start()

print("Main thread continuing execution...")
for thread in threads:
    thread.join()

print("Main thread exiting...")

