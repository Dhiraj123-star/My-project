-- | this is nested if else program
main=do
    let num=10


    if num==0
        then putStrLn "Number is Zero"
    else if num `rem` 2 == 0
        then putStrLn "Number is Even "
    else  putStrLn "Number is odd "
    putStrLn "Thanks For using Haskell Programming Language :)"