//iterator example
const number=[10,20,40,50]
//iterable
for(let n of number[Symbol.iterator]()){
    console.log(n)
    
}