from threading import *

class MyThread(Thread):
    def myDisplay(self):
        for i in range(1,6):
            print("Child Thread")


t = MyThread()
thread=Thread(target=t.myDisplay())
t.start()