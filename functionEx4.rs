// pass by reference

fn main(){
    let mut no:i32 =100;
    mutate_to_zero(&mut no); //passed reference of the number

    println!("the value of no is {}",no)
}
fn mutate_to_zero(para:&mut i32){
    *para=0; //dereference operator, which change value of no.

    
}