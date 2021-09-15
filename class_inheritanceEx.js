//class inheritance example


class parent_class{ //parent class 

    constructor(name){ //parent class constructor
        this.name=name
    }
    display(){
        console.log(`hello ${this.name}`)
    }
}
// derived class 
class derived_class extends parent_class{
    constructor(name)
    {
        super(name) //super keyword,call parent class constructor
    }
    
    display(){  //overriding the parent class method
        console.log(`hello ${this.name}`) 
    }
}

//creating object
let obj=new derived_class("JavaScript") //call the child class constructor

obj.display() //call child class method