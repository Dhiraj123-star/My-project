//another example of variable declaration, this time mutable
fn main(){
    let mut fees:i32 =  25000;
    println!("Fees is {} ",fees);
    fees=23400; //here we changed our value because it is mutable
    println!("The reassigned fees is {}",fees);
    println!("Thanks for using Rust Programming language :)");
}