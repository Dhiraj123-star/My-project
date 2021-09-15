//example of generator 
function *generator_ex(){
    yield 100
    yield 300


}
//creating generators
const mygen=generator_ex()
console.log(mygen.next())
// throws an error
// terminates the generator
console.log(mygen.throw(new Error('Error occurred.')));
console.log(mygen.next());