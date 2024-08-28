import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1,6]
    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something,secs)

    for result in results:   # for map functon we will use this
        print(result)

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')