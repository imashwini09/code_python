import multiprocessing
import time

def hello_world(t):

    time.sleep(t)

    print(f"Hello World! from {multiprocessing.current_process().name}")


time1 = time.perf_counter()

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=hello_world, args=(4,))
    process1.start()
    process1.join()
    time2 = time.perf_counter()
    print(time2-time1)