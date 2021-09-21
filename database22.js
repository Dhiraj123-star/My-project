//drop table if it exist

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

    var sql = "DROP TABLE IF EXISTS NODETABLE "; //DROP THE TABLE IF IT EXISTS 

    con.query(sql, 
    function(err, result){
        if(err) throw err
        console.log(result);

        console.log("Thanks for using Node.js :)");
})

})