--List comprehension example
main=do
    putStrLn "This is the list of the numbers from 1 to 100\n"

    print([y|y<-[1..100]]) --It prints a list of 100 numbers
    
    putStrLn"\n"  --new line

    putStrLn "this is the cube of the numbers\n"

    print([z**3 | z <-[1..5]]) --It prints cube of the numbers in the list