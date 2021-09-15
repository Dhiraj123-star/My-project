//example of javascript generator
function *gen_return(){
    yield 1000
    return 200
    console.log("after return statement")
}
//creating generator
const mygenerator=gen_return()
console.log(mygenerator.next())
console.log(mygenerator.next())
console.log(mygenerator.next())