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

    var sql = "select * from nodetable limit 4"; //limit the records by 4

    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log(result);
})
})