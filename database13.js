//escaping multiple placeholders , the array contains multiple values 

var mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    var address = "Gurgaon"; //provided by the user
    var name="Dhiraj"; //provided by the user
    
    //here we put placeholder for both name and address because both values are provided by user


    var sql= "select * from nodetable where name = ? or address=?";


conn.query(sql,[name,address] ,function(err,result){
    if(err) throw err;

    console.log(result);

})
})
