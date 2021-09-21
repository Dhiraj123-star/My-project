//create table 
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

var sql = "Create table nodetable (name varchar(255), address varchar(255))";
conn.query(sql,function(err,result){
    if(err ) throw err;
    console.log("table created :)");
});
});
