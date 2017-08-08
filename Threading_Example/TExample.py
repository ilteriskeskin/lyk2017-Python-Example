from threading import Thread

import time

class Worker(Thread):
    def run(self):
        while True:
            print("Thread 1 %s " % time.time())
            time.sleep(2)

class Worker2(Thread):
    def run(self):
        while True:
            print("Thread 2 %s " % time.time())
            time.sleep(2)

if __name__ == '__main__':
    work1 = Worker()
    work1.start()

    work2 = Worker2()
    work2.start()
