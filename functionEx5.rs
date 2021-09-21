//find the area of triangle
fn main(){
    //set the value of base
    let base :f64 = 12.0;

    //set the height 
    let height:f64 = 6.0;

    //call the function
    area_tri(base,height);
}
fn area_tri(b:f64, h:f64){
        let area= 0.5*b*h;

    println!("The area of the triangle is {}",area);
}