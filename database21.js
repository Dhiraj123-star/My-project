//drop  table
//limit the records
var mysql= require('mysql');

var con= mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"rootpassword",
    database:"node"
})
console.log("Database connected successfully :)");
con.connect(function(err){
    if(err) throw err;

    var sql = "drop table nodetable"; //drop nodetable

    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log("Table deleted successfully :)");
})
})