// select all records where the address starts with the letter 'R'
//where clause 
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    //select all records where address starts with 'R' 

conn.query("select * from nodetable where address like 'R%'", function(err,result){
    if(err) throw err;

    console.log(result);

})
})