from multiprocessing import Process
import os
import time

# io bound job so gil release and python do work many threads
# but we use multi process so create isolated process for each task
def go_to_sleep(n):
    time.sleep(0.5)

# cpu bound job so for real parallel in cpu bound tasks we need use multi process instead thread or async
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == '__main__':

    processes = [
        Process(target=go_to_sleep, args=[30]) for i in range(10)
    ]

    start = time.time()
    
    for p in processes:
        p.start()
    
    print(f'PID = {os.getpid()}')

    for p in processes:
        p.join()
    
    end = time.time()

    print(f"done with : {end-start}")
