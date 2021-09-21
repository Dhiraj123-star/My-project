var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err, db){

    if(err) throw err;

    var dbo = db.db("node");

    

    dbo.collection("customers").find({}).toArray(function(err, result){ //change into the array

        if(err) throw err;


        console.log(result);

        db.close();
    })
})