//class example in js

class myclass{ //class
    constructor(name){ //automatically call when any object is created 
        this.name=name
    }
    greet(){
        console.log(`hello ${this.name}`)
    }
}
//creating object
let p1=new myclass("Dhiraj");

console.log(p1.name); //access the class property

//calling the class method

p1.greet();

console.log("Thanks for using javascript :)")


