//scalar data types in rust
fn main(){
    let result=10; //i32 by default
    let age:i32 =22;
    let sum:i32 = 100+23;
    let sub:i32 = 30 -90; 
    let mark : isize=100; /*it means the size of the data type will 
    derived from architecture of the machine */
    let count:usize =50; //unsigned size
    
    println!("the result is {}",result);
    println!("the age is {}",age);
    println!("the sum {} and sub {} ",sum,sub);
    println!("the mark {} and count {} ",mark,count);


}