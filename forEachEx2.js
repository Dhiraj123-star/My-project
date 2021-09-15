const Array1=["Ramesh","Suresh","Raju","Karan"]
console.log("the original array is: ",Array1)
const Cpy_array=[]
Array1.forEach(function(item){
    Cpy_array.push(item)
})
console.log("the copied array is: ", Cpy_array)
//forEach with set
const myset=new Set([1,3,5,3,6,8])
//looping through set
console.log("Looping through the set :)")
myset.forEach(myfunction)
function myfunction(item){
    console.log(item)
}
//map example
let mymap=new Map()
mymap.set(1,"Java")
mymap.set(2,"Python")
mymap.set(3,"TypeScript")
//looping through map
console.log("Iterating through map :)")
mymap.forEach(myfunction)
function myfunction(value,key){
    console.log(key,value)
}
