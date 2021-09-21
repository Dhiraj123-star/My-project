var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err, db){

    if(err) throw err;

    var dbo = db.db("node");

    var query = {"address":"Gurgaon"};

    //only returns where address  is Gurgaon in the documents


    dbo.collection("customers").find(query).toArray(function(err, result){ 

        if(err) throw err;


        console.log(result);

        db.close();
    })
})