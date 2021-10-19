# permutation of words using python

import itertools

value = input("Enter your value: ")
nums= list(value)


permutations = list(itertools.permutations(nums))

print([' '.join(permutation) for permutation in permutations])