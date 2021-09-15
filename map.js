//this is the map example in Js
let map1=new Map();
//insert key-value pair
map1.set('info',{name:"mack","age":34})
console.log(map1) 
//getting value from the map
console.log("The value is:",map1.get('info'))
//checking element in the map
console.log(map1.has('info')) //true
console.log(map1.has('name')) //false
//deleting elements from the map
console.log(map1.delete('myinfo')) //returns false
console.log(map1)
console.log(map1.delete('info')) //returns true
console.log("Map after deleting:",map1) 
//another map example
let map2=new Map()
map2.set('detail',{'name':"pratham",'age':18})
console.log("another map is: ",map2)
//clear () method
map2.clear()
console.log("After using clear():",map2)


