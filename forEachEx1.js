//forEach example in js
myarray=["Java","JavaScript","Python","Scala"]
myarray.forEach(element => { //using arrow function

    console.log(element)
    
});
console.log("using another method :)")
myarray.forEach(myfunction) //another method

function myfunction(item){
    console.log(item)
}
//updating elements of the array
myarray.forEach(update_func)
function update_func(item,index,arr){
    arr[index]='hello' +item
    console.log(myarray)
}
console.log("outside the function is: ",myarray)