--this is another list function example
main=do
    let my=[12,18,50,20] --this is the list
    putStrLn "Our list is: "
    print(my)
    putStrLn "The summation of the list element is: "
    print(sum my) --returns total sum of all elements 
    let my1=[1..10]
    putStrLn "The list is: "
    print(my1) --this is the another list
    putStrLn "The multiplication of the list elements are: "
    print(product my1)
    let my3=[12,5,8,78]
    putStrLn "Does it contain 8 ??" 
    print (elem 8(my3)) --check existance of the particular element in the list , it returns true
    print(elem 10 (my3))  --returns false
