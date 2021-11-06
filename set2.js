//chaining of the set
let myset = new Set();
myset.add("Ram").add("Ramesh").add("Shyam"); //chaining of the set by using multiple add method
//returns set data
console.log("The list of set values: ");
console.log(myset);
//iterate through the set elements
console.log("Iterate using for of loop \n");
for (let mylist of myset) {
    console.log(mylist);
}
//iterate through the set elements using foreach
console.log("Iterate using foreach loop\n");
myset.forEach(function (value) {
    console.log(value);
});
