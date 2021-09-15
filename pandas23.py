import pandas as pd


# python's dictionary act as json

data={
    "name":{
        1:"Dhiraj",
        2:"Yasweer",
        3:"Lokesh",
        4:"Ashish",
        5:"Akash"
    },
    "address":{
        1:"Bhiwadi",
        2:"Rewari",
        3:"Bhiwadi",
        4:"Rewari",
        5:"Bhopal"
    },
    "age":{
        1:22,
        2:23,
        3:20,
        4:19,
        5:21
    },
    "hobby":{
        1:"Coding",
        2:"Hacking",
        3:"Playing",
        4:"Gaming",
        5:"Reading"
    }
}

df=pd.DataFrame(data)

print(df.to_string())