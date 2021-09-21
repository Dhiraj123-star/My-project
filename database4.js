var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, function(err,db){
    if(err) throw err;

    var dbo= db.db("node");

    var myobj=[

        {"name":"Pratham","address":"Bhiwadi"},
        {"name":"Prakash","address":"Gurgaon"},
        {"name":"Puja","address":"Noida"},
        {"name":"Gajendra","address":"Jaipur"},
        {"name":"Dhara","address":"Bhiwadi"},
        {"name":"Sumit","address":"New Delhi"},
        {"name":"Anup","address":"Gurgaon"},

    ]
    dbo.collection("customers").insertMany(myobj,function (err, res){
        if(err) throw err;

        console.log("Number of records inserted "+res.insertedCount);

        db.close();
    })
})