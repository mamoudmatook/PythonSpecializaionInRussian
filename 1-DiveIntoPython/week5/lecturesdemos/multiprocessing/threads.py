from threading import Thread
def hello(name):
    print("hello " + name)

th = Thread(target= hello, args=("bob", ))
th.start()
th.join()