//continue statement in rust
fn main(){
    let mut count=0;
    for num in 1..21{
        if num%2==0{
            continue;
        }
        count=count+1;

    }
    println!("The total no. of odd numbers between 1 to 20 is {}",count);
}