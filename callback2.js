//another example of callback 
function main_fun(prog_name, call_me){
    console.log("Best programming language: ",prog_name)
    call_me()
}
//call back function
function call_me(){
    console.log("welcome in callback function :)")
}
//calling the function
main_fun("JavaScript",call_me)
console.log("Thanks for using JavaScript :)")