var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        var myquery = {address:"Jaipur"}  //delete documents where address is jaipur

        

        dbo.collection("customers").deleteOne(myquery,
            function(err,obj){
                if(err ) throw err

                console.log( "1 document deleted ")

                db.close()
            })

    })