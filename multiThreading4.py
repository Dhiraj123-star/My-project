import threading

# global variable x

x=0

def increment():

    """
    function to increment the global variable
    """

    global x
    x+=1


def thread_task(lock):

    """task for thread
    calls increment function 100000 times """

    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():

    global x

    # setting global variable to 0

    x=0

    # creating a lock

    lock = threading.Lock()

    # creating threads

    t1 = threading.Thread(target=thread_task,args=(lock,))
    t2= threading.Thread(target=thread_task,args=(lock,))

    # start threads

    t1.start()
    t2.start()

    # wait until threads finish its execution

    t1.join()
    t2.join()


if __name__ =="__main__":
    for i in range(200):
        main_task()

        print("Iteration {0}: x= {1} ".format(i,x))