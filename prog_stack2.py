#write a program to display unique vowels present in the given word
#using stack
vowels=['a','e','i','o','u']
word=input("enter the word to search for vowels:")
stack=[]
for letter in word:
    if letter in vowels:
        if letter not in stack:
            stack.append(letter)
print(stack)
print("the number of different vowels present in",word,"is",len(stack))

