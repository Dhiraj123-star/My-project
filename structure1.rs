//structure example in rust
struct Employee{
    name:String,
    company:String,
    age:u32

}
fn main(){
    let emp1 = Employee{
        company :String::from("Dhiraj coder"),
        name:String::from("Dhiraj"),
        age:50
    };
    println!("Name of the company is {}",emp1.company);
    println!("Name of the emloyee is {}",emp1.name);
    println!("Age of the employee is {}",emp1.age);

    println!("Thanks for using Rust Programming Language :)");

}