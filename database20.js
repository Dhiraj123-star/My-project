//delete operation
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

    var sql = "delete from nodetable where id>7"; //delete the records where id is greater than 7

    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log("No. of records deleted", result.affectedRows); //4 records deleted
        console.log(result);
})
})