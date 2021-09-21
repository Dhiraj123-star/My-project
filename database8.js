//select particular columns
var  mysql=require("mysql")

var conn= mysql.createConnection({host:"localhost",user:"root",password:"rootpassword",database:"node"})

conn.connect(function(err){
    if(err ) throw err;
    console.log("connected :)");

    //only returns only id, name from  the table

    conn.query("select id ,name from nodetable",function(err,result,fields){
        if(err) throw err;
        console.log(result);//returns whole records

        console.log("The name of the third record is :");

        console.log(result[2].name); //returns name of the third record

        console.log("The details of the fields :");

        console.log(fields) ; //prints the details of fields

        //returns the name of second field

        console.log("The name of the second field is: ");
        console.log(fields[1].name); //returns name 

        console.log("Thanks for using Node.js :)");

    })
});
