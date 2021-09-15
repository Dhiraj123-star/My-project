# python program to illustrate the concept of multithreading

import threading

import os

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("Id of process running task 1 {}".format(os.getpid()))




def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("Id of process running task 2 {}".format(os.getpid()))


# main program

# print ID of the current process 

print("ID of process running main program: {}".format(os.getpid()))

# print name of the main thread 

print("Main thread name is {}".format(threading.main_thread().name))


# creating threads 

t1 =threading.Thread(target=task1,name="t1")

t2 = threading.Thread(target=task2,name="t2")

# starting the threads

t1.start()

t2.start()

# wait until all threads finish

t1.join()
t2.join()
