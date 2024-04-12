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
                {"Name":"Ishita Chauhan","Age":21,"Dream":"Will marry Mrinal"},
                {"Name":"Avani Chaturvedi","Age":21,"Dream":"Will do AI/Ml"},
                {"Name":"Heli Bhatt","Age":19,"Dream":"Want a Chava"},
                {"Name":"Pranjal Patel","Age":19,"Dream":"I want Aarsh Aatrey"},
                {"Name":"Puja Mahavadiya","Age":22,"Dream":"Jemmy is my dream Husband"},
                {"Name":"Mahek Gor","Age":21,"Dream":"I am an archeoptrix"}]
    
    collection.insert_many(insertHere)