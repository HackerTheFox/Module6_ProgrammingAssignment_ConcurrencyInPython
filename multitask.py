# AUTHOR: Marcus Ed. Butler
# VERSION: 2024-09-27_R0
# DESCRIPTION: Prints out the current time using multitasking.

from random import randint
from time import sleep
import multiprocessing as multi
from datetime import datetime


def task(number):
    wait = randint(0,1)
    sleep(wait)
    print(f"Process {number}:", datetime.now().strftime("%H:%M:%S"))


processes = []
for number in range(1,4):
    # Create process
    p = multi.Process(target=task, args=(str(number)))

    # Keep track of processes.
    processes.append(p)

    # Start process
    p.start()


# Wait for process to end before closing program.
for process in processes:
    process.join()
