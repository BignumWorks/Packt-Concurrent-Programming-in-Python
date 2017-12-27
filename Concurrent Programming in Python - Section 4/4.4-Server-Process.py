from multiprocessing import Process, Manager


def target(number, a):
    print("Appending {}".format(number))
    a[number] = number


if __name__ == "__main__":
    manager = Manager()

    a = manager.list([0]*10)
    threads = [Process(target=target, args=(i, a), name="target-{}".format(i)) for i in range(10)]

    for i in a:
        print(i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for i in a:
        print(i)