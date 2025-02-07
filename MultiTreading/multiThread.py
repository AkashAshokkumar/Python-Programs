import time
import threading

li1 = [1,2,3,4,5,6]
li2 = ['a','b','c','d','e']

def displayDigit(li):
    print(threading.current_thread())
    for i in li:
        print(i)
        time.sleep(1)

def displayLetters(li):
    print(threading.current_thread())

    for i in li:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=displayDigit, args=(li1,))
t2 = threading.Thread(target=displayLetters, args=(li2,))

t1.start()
t2.start()

    

