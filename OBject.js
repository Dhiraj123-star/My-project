//javaScript object example


const obj = {
    "name":"Dhiraj",
    "age":22,
    "hobby" :{
        "reading":true,
        "gaming":false,
        "game":"cricket"

    },
    "class":["JavaScript","Java","C","C++"],

    "myfun":function(){
        console.log("Javascript is fun to learn programming language")
    }


}
console.log(obj.name)//Dhiraj
console.log(obj.age) //22
console.log(obj.hobby["reading"]) //returns true

console.log(obj.class[3]) //returns C++

console.log(obj.class[4]) //returns undefined 


obj.myfun() //calling the function