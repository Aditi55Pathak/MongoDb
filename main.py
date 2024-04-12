import pymongo

if __name__=="__main__":
    print("Welcome to pyMongo")
# Create a mongoCLient which will help to connect to the database 
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['Aditi']
    collection=db['mySampleCollection']
    # dict={"Name":"Aanya Malhotra", "Age":"20", "Dream":"Rich and Successfull"}
    # collection.insert_one(dict)

    insertHere=[{"Name":"Aditi Pathak","Age":20,"Dream":"Will buy & BHK"},
                ]

