import os
from time import sleep
from threading import Thread
import time

# io bound job so gil release and python do work many threads
def go_to_sleep(n):
    sleep(0.5)


# cpu bound job so gil just use one thread and python work like sequential
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":

    threads = [
        Thread(target=go_to_sleep, args=[30]) for i in range(20)
    ]

    start = time.time()
    
    [t.start() for t in threads]
    
    print(f'PID = {os.getpid()}')
    
    [t.join() for t in threads]

    end = time.time()

    print(f"done with : {end-start}")