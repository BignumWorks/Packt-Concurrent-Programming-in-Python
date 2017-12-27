from threading import Thread


def target(number, a):
    print("Appending {}".format(number))
    a.append(number)


if __name__ == "__main__":
    a = []
    threads = [Thread(target=target, args=(i, a), name="target-{}".format(i)) for i in range(10)]

    print("Before Processing: {}".format(a))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("After Processing: {}".format(a))
