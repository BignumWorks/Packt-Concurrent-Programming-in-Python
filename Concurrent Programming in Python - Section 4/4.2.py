from multiprocessing import Process, current_process
from threading import Thread
import time

def calculate_factorial(number):
    #print("Starting Process:{} with pid:{}".format(current_process().name, current_process().pid))
    fact = 1

    for i in range(1, number):
        fact *= i

    return fact


if __name__ == "__main__":
    num = 100000
    num_processes = 2
    processes = []

    start = time.time()
    for i in range(num_processes):
        process_name = "Process {}".format(i)
        p = Process(target=calculate_factorial, args=(num,), name=process_name)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("Processes: It took {} seconds with {} processes".format(end-start, num_processes))

    processes = []

    start = time.time()
    for i in range(num_processes):
        process_name = "Thread {}".format(i)
        p = Thread(target=calculate_factorial, args=(num,), name=process_name)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print("Threads: It took {} seconds with {} threads".format(end - start, num_processes))