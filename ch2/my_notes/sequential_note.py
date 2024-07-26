import time
import os


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == '__main__':

    print(f'PID = {os.getpid()}')
    
    start = time.time()

    for i in range(20):
        fibonacci_recursive(30)

    end = time.time()

    print(f"done with : {end-start}")