//factorial program in js
function factorial(num){
    if(num<0){
        console.log("number should be positive :)")
    }else{
    if(num==0){
        return 1
    }
    else{
        return num*factorial(num-1)
    }
}
}

//calling the function

 result= factorial(5) //returns 120 :)
 console.log("The factorial is: ",result)

 result1 = factorial(-10) //returns undefined 
 console.log("The factorial is: ",result1)
 