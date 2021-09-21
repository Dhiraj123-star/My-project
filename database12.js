//escape query values with placeholder

var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    var address = "Gurgaon"; //provided by the user
    
    //returns all records from address Gurgaon

    var sql= "select * from nodetable where address =?";


conn.query(sql,[address] ,function(err,result){
    if(err) throw err;

    console.log(result);

})
})
