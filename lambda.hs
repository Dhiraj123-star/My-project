--this is lambda function
main=do
    putStrLn"The successor of 10 is:"
    print((\y -> y + 1)10)
    putStrLn "Another example of lambda function :)"
    putStrLn "The power of 10 is:"
    print((\z -> z**2)10)