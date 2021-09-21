//insert value into the table 
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

var sql = "insert into  nodetable values('Dhiraj', 'Bhiwadi',1)"; //insert single record into the table
conn.query(sql,function(err,result){ 
    if(err ) throw err;
    console.log("one record inserted  :)");
});
});
