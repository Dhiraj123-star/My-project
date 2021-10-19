--using take function which create sub-string from another string
main =do 
    print("The substring is :",take 10 ([1..100]))
    print("Using Drop",drop 10([1..100]))  --drop the first 10 numbers from the list

    let mylist = [10,67,2,45,22,101]  --this is the list
    putStrLn "The maximum value element of the list is: "
    print(maximum mylist)  --returns maximum value
    putStrLn "The minimum value element of the list is: "
    print(minimum mylist) --returns minimum value 
    