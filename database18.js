//start the position 3 and returns the next  5 records

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

    var sql = "select * from nodetable limit 5 offset 2"; //printing the five records from 3 rows



    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log(result);
})
})