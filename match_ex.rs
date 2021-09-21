//match statement in rust
/* match statement is just like switch in c , returns which one of the following
expression will match :) */
fn main(){
let day = "Sunday";
let myday= match day {
    "Monday" =>{ println!("Found !! Your first day"); "Monday"},
    "Tuesday"=>{ println!("Found !! Your second day"); "Tuesday"},
    "Wednesday"=>{ println!("Found !! Your third day"); "Wednesday"},
    "Thursday"=>{ println!("Found !! Your fourth day"); "Thursday"},
    "Friday" => { println!("Found !! Your fifth day"); "Friday"},
    "Saturday"=>{ println!("Found !! Your sixth day"); "Saturday"},
    "Sunday" => { println!("Found !! Your seventh day"); "Sunday"},
    _ => "Unknown" //this is just like default statement
};
println!("Your day is {}",myday);

}