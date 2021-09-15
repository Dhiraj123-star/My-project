//another example of generator in javascript

function *mygenerator(){
    console.log("1. before the first yield")

    yield 100
    console.log("2. before the second yield")

    yield 200

    console.log("3. before the third yield")

}
//creating generators

const mygen = mygenerator()

console.log(mygen.next())
console.log(mygen.next())
console.log(mygen.next())