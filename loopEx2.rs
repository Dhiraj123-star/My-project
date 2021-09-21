//while loop example in rust
fn main(){

    let mut x=0; // make x mutable so that we can assign value twice to it 

    while x<10{ //while loop example
        x+=1;
        println!("Inside the loop x is {}",x);
    }
    println!("outside the loop , the x is {}",x);

    println!("Thanks for using Rust Programming Language :)");
}