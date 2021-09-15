//another example of object in javascript
const myobject={
    name:"Dhiraj",
    age:23,
    subject:{ //nested properties
        first:"Networking",
        second:"Programming",
        third: "cyber security"
    },
    hobby:"coding"

}
console.log(myobject) //prints the whole object

console.log(myobject.subject.first)//accessing the first in subject
console.log(myobject["hobby"]) //returns coding
 
