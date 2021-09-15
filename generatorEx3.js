//another example of generator in javascript
function *gen1(){
    
    let y= yield "Hello JavaScript"

    console.log(y)
    console.log("Some code here")
    yield 100

}
//create generators

const mygen =  gen1()
console.log(mygen.next())
console.log(mygen.next(6))
console.log(mygen.next())