--factorial program in Haskell
fact::Integer->Integer
fact 0=1
fact n=n*fact(n-1)
main=do
    putStrLn "The factorial of 5 is: "
    print(fact 5) 
    putStrLn"Thanks For using Haskell Programming :)"