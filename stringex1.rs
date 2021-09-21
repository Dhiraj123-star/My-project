fn main(){
    let company:&'static str ="Dhiraj Programmer";
    let location:&'static str = "Bhiwadi";
    println!("company is :{} location :{} ",company,location);
    
    //another way of defining the string in rust
    let empty_string =String::new();
    
    //find the length of the string
    println!("Length is: {}",empty_string.len()) ; 

    let content_string= String::from("Rust Programming");
    println!("The length is: {}",content_string.len());
    print!("Thanks for using Rust Programming language :)")
}