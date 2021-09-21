var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        var myquery = {"address": "Noida"}

        var newValue = {$set:{name:"Manjeet", address:"Lucknow"}}

        dbo.collection("customers").updateOne(myquery,newValue,
            function(err,res){
                if(err ) throw err

                console.log("1 document updated")

                db.close()
            })

    })