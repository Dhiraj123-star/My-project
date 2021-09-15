//recursive function example in js 
function countnum(num){ 
    console.log(num)
    //increase the number
    const increase_num=num+1 //increase one recursively 

    if(increase_num<=0){ //base condition
        countnum(increase_num)
    }
}
//calling the function
countnum(-7)
