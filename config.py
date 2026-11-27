from pymongo import MongoClient

from decouple import config

uri=config("MONGO_URI")
client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")

db = client["your_db"]
collection = db["users"]  # ✅ Remains open for FastAPI routes to use