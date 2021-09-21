//order by desc

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

    con.query("select * from nodetable order by id desc" , //order by id  in descending order
    function(err, result){
        if(err) throw err
        console.log(result);
})
})
