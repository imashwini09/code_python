# How to pass arguments

import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} sec(s)')
    time.sleep(seconds)
    print('Done SLeeping')


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])  # thread execution
    # t = threading.Thread(target=do_something(1.5))   # Function calling output will be different
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
    
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')