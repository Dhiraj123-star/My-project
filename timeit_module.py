import timeit

# code to be executed only once
setup_code ="import math"

# code whose execution time is to be measured

stmt_code = """
def square_root():
    return math.sqrt(4)"""


#return execution time with 500 iterations

print(timeit.timeit(stmt=stmt_code,setup=setup_code,number=500))
