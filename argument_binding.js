//argument binding in javascript
let x=function(){
    console.log(arguments) //this is called argument binding

}
x(10,45,56,66) //calling the function

//argument binding achieved in arrow function by spread operator

let y=(...n)=>{ //spread operator
    
    console.log(n)
}
y(10,20,30,40) //calling the arrow function