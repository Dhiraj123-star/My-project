//inserting multiple records 


var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

var sql = "insert into nodetable (name,address) values ?"; //adding placeholder for multiple records 

var values=[
    ['Pratham','Bhiwadi'],
    ['Prakash','Gurgaon'],
    ['Rohit','Bhiwani'],
    ['Yasweer','Rewari'],
    ['Gajendra','Rewari'],
    ['Lokesh','Bhiwadi'],
    ['Ramesh','Gurgaon'],
    ['Ram','Bhiwani'],
    ['Ashish','Bhiwadi'],


]

conn.query(sql,[values],function(err,result){
    if(err ) throw err;
    console.log("No. of records inserted : ", result.affectedRows); //returns 9
});
});
