//another example of parameterised function

fn main(){
    let name:String =String::from("Dhiraj Rust Programmer");

    display(name); //calling the function
    
}
fn display(para:String){
    println!("the string is {}",para);
}