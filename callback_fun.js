//callback function in javaScript

function greet(name,callback){
    console.log("Hello ",name)
    callback()
}

    function callme(){
        console.log("I'm callback function :)")
    
}
//now calling the function
greet("Dhiraj",callme)