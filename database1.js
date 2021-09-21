var mongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

mongoClient.connect(url,function(err,db){
    if(err) throw err;
    console.log("Database Created :)")
    db.close()
})