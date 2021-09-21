var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database

MongoClient.connect(url,
    function(err,db){

        if(err) throw err

        var dbo= db.db("node")

        var myquery = {address:/^B/}  //delete as many document where address is Bhiwadi

        

        dbo.collection("customers").deleteMany(myquery,
            function(err,obj){
                if(err ) throw err

                console.log( obj.result.n, " document(s) deleted ")

                db.close()
            })

    })