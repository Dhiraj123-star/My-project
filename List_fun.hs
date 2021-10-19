--List and its functions
main=do
    let x=[1..10] --list 
    putStrLn "Our List is: "
    print(x)
    putStrLn "The First element of the list is: "
    print(head x) --prints the first element
    putStrLn "The tail  of the list is: "
    print(tail x)  --prints the entire list without the head part i.e first 
    putStrLn "The last element of the list is: "
    print(last x) --prints the  last element of the list
    putStrLn "The list without the last entry: "
    print(init x) --returns the entire list without last entry , it is opposite of tail
    putStrLn "Is our list empty??"
    print(null x) --it returns true if list is empty otherwise returns false
    let y=[]
    putStrLn "Is Our list empty ???"
    print(null y)
    putStrLn "The list in the  reverse order is: "
    print (reverse x) --returns the list in reverse order 
    putStrLn "The Length of the  first list is: "
    print(length x) --returns length of the list
    putStrLn "The Length of the second list is: "
    print(length y) --returns length of the list
    putStrLn "Thanks For Using Haskell Programming Language :)"
