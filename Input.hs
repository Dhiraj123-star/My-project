-- |This is comment in Haskell
main=do
    putStrLn "Enter Your Favourite Programming Language"
    name <- getLine
    putStrLn ("Your Favourite Programming Language is: "++ name)
    putStrLn "Enter Your age: "
    age<-getLine
    putStrLn("Your age is :" ++ age)
