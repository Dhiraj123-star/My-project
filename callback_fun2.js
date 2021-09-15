//another example of callback fun() with sychronous method
function greetme(name, call_me){
    console.log("Welcome in JavaScript Programming")
    //callback function only executed after greetme()
    call_me(name)
    
}
function callsomething(name){
    console.log("Hello "+name)
}
//calling the function by setTimeout() after 2 secs
setTimeout(greetme,2000,"Dhiraj",callsomething)