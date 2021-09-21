//select statement

var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");
conn.query("Select * from nodetable",function(err, result,fields){
    if(err) throw err;
console.log(result);
})
})