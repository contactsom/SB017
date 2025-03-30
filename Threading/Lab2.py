from threading import *

def currentThread():
    for i in range(1,6):
        print("**** I am Chile Thread ****")


t=Thread(target=currentThread()) # Thread Object Created
t.start() # Thread Started