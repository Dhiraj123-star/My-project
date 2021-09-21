var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err, db){

    if(err) throw err;

    var dbo = db.db("node");

    //find the first records from the documents

    dbo.collection("customers").findOne({},function(err, result){

        if(err) throw err;

        console.log(result.name);  //returns the name of the record

        console.log(result);

        db.close();
    })
})