//javascript getter and setter method

class myclass{
    constructor (age){
        this.age=age
    }
    //get method
    get person_age(){
        return this.age
    }
    //set method
    set person_age(x){
        this.age=x
    }
}
//creating object

let obj=new myclass(22);

console.log(obj.age) //returns 22

//set the age  with the help of setter method 
obj.person_age=21 
console.log(obj.person_age) //returns 21, by getter method