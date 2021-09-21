//add primary key into the existing table

var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

var sql = "alter table nodetable add column id int auto_increment primary key"; //alter the table

conn.query(sql,function(err,result){
    if(err ) throw err;
    console.log("table altered  :)");
});
});

