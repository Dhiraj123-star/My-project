var mongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

mongoClient.connect(url,function(err,db){
    if(err) throw err;
    var dbo = db.db("node")
    var myobj={name:"Dhiraj","address":"Bhiwadi"};
    dbo.collection("customers").insertOne(myobj,function(err,res){
        if(err) throw err;
        console.log("\n 1 document inserted :)")
        db.close() //closing the resources
    })

})