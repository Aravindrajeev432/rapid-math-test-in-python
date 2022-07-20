from time import *
import threading
import random

score = 0


def countdown():
    global timer
    timer = 15
    for x in range(15):
        print(timer)
        timer = timer - 1
        sleep(1)
    print("out of time")


countdown_thread = threading.Thread(target=countdown())

while True:
    s = input("Can we start y/n")
    if s == "y":
        countdown_thread.start()
    else:
        break
