import threading 
shared_variable = 0

mutex = threading.Lock()

def addr():
    global shared_variable
    for _ in range(1000000):
        mutex.acquire()
        shared_variable += 1
        mutex.release()

def subr():
    global shared_variable
    for _ in range(1000000):
        mutex.acquire()
        shared_variable -= 1
        mutex.release()

thread1 = threading.Thread(target=addr)
thread2 = threading.Thread(target=subr)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(shared_variable)