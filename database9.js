//where clause 
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    //select all records where address is Bhiwadi

conn.query("select * from nodetable where address='Bhiwadi'", function(err,result){
    if(err) throw err;

    console.log(result);

})
})