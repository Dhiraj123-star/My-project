var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err, db){

    if(err) throw err;

    var dbo = db.db("node");

    var myobj =[

        {"_id":1,"name":"Sachin","address":"Rewari"},

        {"_id":2,"name":"Sachi","address":"Noida"},

        {"_id":3,"name":"Tanmay","address":"New Delhi"},
        
    ];

    dbo.collection("customers").insertMany(myobj,function(err, res){

        if(err) throw err;

        console.log(res);

        db.close();
    })
})