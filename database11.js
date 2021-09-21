//escape character
var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    var address = "Bhiwani"; //provided by the user
    
    //returns all records from address Bhiwani

    var sql= "select * from nodetable where address =" + mysql.escape(address);


conn.query(sql, function(err,result){
    if(err) throw err;

    console.log(result);

})
})
