from pymongo import MongoClient

client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
    
db = client["user_db"]
collection = db["users"]