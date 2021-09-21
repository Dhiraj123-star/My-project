//retriewing ids
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");
var sql= "insert into nodetable (name,address) values('Roshan', 'Rewari')";
conn.query(sql, function(err,result){
    if(err) throw err;
    console.log("1 record inserted ID is: ",result.insertId); //returns the id of inserted record
})
})
