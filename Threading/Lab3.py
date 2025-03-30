from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print("Child Thread")


t = MyThread()
t.start()