from multiprocessing import Process, Array

__author__ = "Mithun"


def target(number, arr):
    print("Appending {}".format(number))
    arr[number] = number


if __name__ == "__main__":
    a = Array('i', 10)

    processes = [Process(target=target, args=(i, a), name="factorial") for i in range(10)]

    for i in a:
        print(i)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    for i in a:
        print(i)
