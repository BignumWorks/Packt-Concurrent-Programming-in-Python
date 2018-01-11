from multiprocessing import Process, Value, Lock

__author__ = "Mithun"


def increment(num, lock):
    for _ in range(1000):
        with lock:
            num.value = num.value + 1


def decrement(num, lock):
    for _ in range(1000):
        with lock:
            num.value = num.value - 1


if __name__ == "__main__":
    num = Value('i', 0)
    print(num.value)

    lock = Lock()

    p1 = Process(target=increment, args=(num, lock))
    p2 = Process(target=decrement, args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)
