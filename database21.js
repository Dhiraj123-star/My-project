var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        //drop collection customers
        

        dbo.dropCollection("customers", function(err,delOk)
        
        {

            if(err) throw err

            if(delOk)

            console.log("Collection deleted :)")

        })
                db.close()
            })

    