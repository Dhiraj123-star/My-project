//string and its methods example in rust

fn main(){
    let prog_name="Java is Best Programming Language".to_string();
println!("Before Replacing, the string is:{}",prog_name);

    //replace java with Rust
    let replace_str=prog_name.replace("Java","Rust");
    println!("The replaced string is: {}",replace_str);


    /*as_str() method extracts a string slice
     containing the entire string */
     let example_str="This is example string".to_string();
     print_literal(example_str.as_str());

     fn print_literal(data:&str){
         println!("Displaying string literal: {}",data);
     }

  /*push() appends the single character 
  to the end of the string */

  let mut mystr=String::from("This is Rus");
  //adding 't' as a character by using push()
  mystr.push('t');

  println!("After pushing the character: {}",mystr);

  //adding string at the end by using push_str() method

  let mut prog = "This is rust ".to_string();
  //adding programming at the end of the string

  prog.push_str("Programming");

  println!("After pushing the string: {}",prog);
  
 println!() ; //new line

  print!("Thanks for using Rust Programming language :)");



}