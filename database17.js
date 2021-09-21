var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        //only returns 4 records as there is mentioned limit 4

        dbo.collection("customers").find().limit(4).toArray(function(err,result)
        {
                if(err ) throw err

                console.log(result)

                db.close()
            })

    })