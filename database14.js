//order by clause

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

    con.query("select * from nodetable order by name" , //order by id by default in ascending order
    function(err, result){
        if(err) throw err
        console.log(result);
})
})