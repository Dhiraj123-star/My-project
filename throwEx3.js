const num=100

try{
    throw new Error("This is the throw statement")
}
catch(error){
    console.log("An error occured")
    if(num+8>100){
        console.log("error message: "+error)
        console.log("Error resolved")
    }
    else{
        throw new Error("the value is low")
    }

}
