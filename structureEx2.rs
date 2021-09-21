//another structure example in rust
struct Programmer{
    name :String,
    age:i32

}
fn main(){
    let mut prog1= Programmer{
        name:String ::from("Dhiraj Programmer"),
        age:23
    }; //adding semicolon is mandatory

    println!("before the changing the value of age :)");
    println!("{}",prog1.age);
    //change the value of age
    prog1.age=24 ;

    println!("Name of the programmer is: {}",prog1.name);

    println!("Age of the programmer is: {}",prog1.age);
}