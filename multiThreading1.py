# python program to illustrate multithreading

import threading

def print_cube(num):

    # function to print the cube of the given number

    print("Cube is: {}".format(num**3))

def print_square(num):

    #function to print the square of the given number
    print("Square is {}".format(num**2))


# main program

t1 = threading.Thread(target=print_cube,args=(10,))

t2 = threading.Thread(target=print_square,args=(12,))

# starting thread1 

t1.start()

# starting thread2

t2.start()

# wait until thread 1 is completely executed 

t1.join()

# wait until thread 2 is completely executed

t2.join()

# both threads completely executed 

print("Done!!!")

