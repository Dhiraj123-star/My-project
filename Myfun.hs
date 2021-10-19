--this is another example of haskell function
myfun::Integer -> Integer -> Integer
myfun a b = a*b
main =do
    putStrLn "The Multiplication function"
    print(myfun 12 5)