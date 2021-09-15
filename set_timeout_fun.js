//setTimeout()
function greet(){
    console.log("Welcome in normal function")
}
function sayname(name){
    console.log("Hello "+ name)

}
setTimeout(greet,2000) //wait for 2000 milliseconds or 2 secs
console.log("Thanks for using javaScript :)")
sayname("JavaScript")