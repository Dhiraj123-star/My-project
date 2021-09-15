//another example of generator
function *mygen(){
    yield 100
    yield 200
    yield 300
    yield 400
    yield 500
}
//create generator
const mygenerator =mygen()

//iterate through the generator
for(let value of mygenerator){
    console.log(value)
    console.log("Thanks for using JavaScript :)")
}