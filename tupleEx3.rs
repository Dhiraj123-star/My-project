//passing tuple inside the function
fn main(){

    //declaring tuple

    let mytuple=("Python",1,"Java",2,"Php",3,"TypeScript",4);

    println!("The tuple is {:#?}",mytuple);

    //passing tuple as parameter
    tuple_fun(mytuple);
}
/* we have to explicitly defined
     type of elements of the tuple*/
fn tuple_fun(mytuple1:(&str, i32, &str, i32, &str, i32, &str, i32)){ 
    
    println!("Inside the function , {:?}",mytuple1);


 println!(); //for new line

println!("Thanks for using Rust Programming Language :)");

}