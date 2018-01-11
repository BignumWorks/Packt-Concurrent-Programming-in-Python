import urllib3
import threading

urllib3.disable_warnings()

__author__ = "Mithun"


def download_url(file_name, url):

    print("Thread {} is called from {}".format(threading.current_thread().name, threading.main_thread().name))
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
    thread = threading.Thread(target=download_url, name=key, args=(key, test_dict[key]), daemon=True)
    print("State of thread Before start {}: {}".format(thread.name, repr(thread)))
    threads.append(thread)
    thread.start()
    print("State of thread After start {}: {}".format(thread.name, repr(thread)))

print("Main thread continuing execution...")
for thread in threading.enumerate():
    print("Thread name is {}".format(thread.name))
    if thread is threading.main_thread():
        continue
    thread.join()

for thread in threads:
    print("Thread {} is Alive? {}".format(thread.name, thread.isAlive()))
    print("State of thread Before start {}: {}".format(thread.name, repr(thread)))

print("Main thread exiting...")
