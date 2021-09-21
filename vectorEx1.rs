//vector example in rust
fn main(){

let mut myvector=Vec::new(); //creating empty vector

myvector.push(100);
myvector.push(200);
myvector.push(300);

println!("The size of the vector is {}",myvector.len()); //find the length of the vector

println!("The vector is {:?}",myvector);

}