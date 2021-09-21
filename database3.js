var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function (err, db){

        if(err) throw err;

        var dbo =db.db("node");

        var myobj= {"name":"Yasweer","address":"Rewari"};

        dbo.collection("customers").insertOne(myobj, function(err,res)
        {
            if(err) throw err;

            console.log("1 document inserted ")

            db.close();
        })
    })