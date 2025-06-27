# Multiprocessing means running multiple processes at once 

import multiprocessing
import time

def task(name):
    print(f"Task {name} starting...")
    time.sleep(2)
    print(f"Task {name} done!")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task, args=("A",))
    p2 = multiprocessing.Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished!")
