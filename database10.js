var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err, db){

    if(err) throw err;

    var dbo = db.db("node");

    //only returns address  of the documents


    dbo.collection("customers").find({},{projection:{_id:0,address:1}}).toArray(function(err, result){ 

        if(err) throw err;


        console.log(result);

        db.close();
    })
})