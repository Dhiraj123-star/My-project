//another example of tuple in rust
fn main(){

    //declaring tuple

    let mytuple =("Dhiraj",22, "Coding",88.3);

    //here the details of the student
    /* we can the tuple elements by dot operator specifying
    its tuple name and index value */

    println!("the name of the student is: {}",mytuple.0);
    println!("the age of the student is: {}",mytuple.1);
    println!("the hobby of the student is: {}",mytuple.2);
    println!("the marks of the student is: {}",mytuple.3);

    println!("Thanks for using Rust Programming language :)");
}