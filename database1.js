var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)")
    conn.query("create database node",function(err,result){
        if(err) throw err;
        console.log("Database created")
    })
})