const num = 100

try{
    if (num<50){
        console.log("Successful :)")

    }else{
        //user defined throw statement

        throw new Error("The number is low")


    }
}catch(error){
    console.log("Error is occured ");

    console.log("Error message : "+ error)
}