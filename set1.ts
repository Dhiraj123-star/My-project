//set concept in typescript

let studentEntries =new Set();

//add values

studentEntries.add("Rahul")
studentEntries.add("Ramesh")
studentEntries.add("Roshan")
studentEntries.add("Ramesh")  //here duplicate entry but it removes it 
studentEntries.add("Tanmay")

//returns set data

console.log(studentEntries)

//check value is present or not

console.log(studentEntries.has("Dhiraj")) //returns false
console.log(studentEntries.has("Ramesh")); //returns true

//it returns the size of the set

console.log("the size of the set is: ",studentEntries.size)

//delete the value from the set

console.log(studentEntries.delete("Roshan")) //delete Roshan from the set

console.log("the size of the set after deletion: ",studentEntries.size)

//clear the whole set

studentEntries.clear()

console.log("after the clear method: ",studentEntries)




