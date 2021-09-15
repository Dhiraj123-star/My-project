//example of map iteration
let itermap=new Map()
itermap.set(1,"JavaScript")
itermap.set(2,"Python")
itermap.set(3,"Ruby")
itermap.set(4,"PHP")
itermap.set(5,"TypeScript")
//iterate through the map keys
console.log("The keys of the map: \n")
for(let keys of itermap.keys()){
    console.log(keys)
}
//iterate through the map values
console.log("\n The values of the map is:\n")
for(let values of itermap.values()){
    console.log(values)
}
//iterate through map keys and values
console.log("\n map keys and values\n")
for(let elem of itermap.entries()){
    console.log(`${elem[0]}: ${elem[1]}`)

}
