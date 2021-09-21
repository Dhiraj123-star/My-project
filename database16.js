var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        var myquery = {address:/^R/}  //update all documents where address starts with R

        var newValue = {$set:{ address:"Alwar"}}

        //update as many records where address starts with R

        dbo.collection("customers").updateMany(myquery,newValue,
            function(err,res){
                if(err ) throw err

                console.log(res.result.nModified, "document(s) updated ")

                db.close()
            })

    })