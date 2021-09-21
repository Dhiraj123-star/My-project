var MongoClient= require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/node" //node is new database


MongoClient.connect(url, 
    function(err, db){


        if(err) throw err;

        var dbo=db.db("node")

        var mysort = {_id :-1}

//sorting by id by descending

        dbo.collection("customers").find().sort(mysort).toArray(function(err,result){

            if(err) throw err

            console.log(result);

            db.close()
        })
    })