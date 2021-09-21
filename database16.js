//update table

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

    var sql = "update nodetable set address= 'Bhiwadi' where id=11"; //update the address where id is 11

    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log(result.affectedRows +"record(s) updated ");
})
})