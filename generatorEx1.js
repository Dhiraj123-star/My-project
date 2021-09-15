//generator example in javaScript

function* generatorfun(){
    console.log("1. code before the first yield")

    yield 1000;
    console.log("2. code after the second yield ")

    yield 2000;
}
//creating generators

const mygen=generatorfun()

console.log(mygen.next()) //returns 1000

console.log(mygen.next()) //returns 2000

console.log(mygen.next()) // { value becomes undefined , done :true }