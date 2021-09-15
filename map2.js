//another example of map
let map1=new Map()
map1.set('detail',{name:'ramesh',id:121})
console.log("the map is: ",map1)
//using size method
console.log("The size of the map is: ",map1.size)
//another map
let mymap=new Map()
mymap.set(1,"java")
mymap.set(2,'python')
mymap.set(3,'C++')
mymap.set(4,'C')
console.log("Another map is: ",mymap)
//iterate through the map
console.log("iterate using for loop :)")
for(let [key,value]of mymap){
    console.log(key,"-",value)
}
//iterate using forEach loop
console.log("Iterate using forEach loop :)")
mymap.forEach(function(key,value){
    console.log(key,"-",value)
})