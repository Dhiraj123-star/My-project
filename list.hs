main=do

    let mylist=[12,45,4,66] --this is haskell list 
    putStrLn "The List is:"
    print(mylist)
    --let mylist2=[100,34,45,a]  throw error because list elements must be homogeneous that means same type
    --putStrLn "Another List is "
    --print(mylist2)
    print([x**2 |x<- [1..10]]) --this is list comprehension example

