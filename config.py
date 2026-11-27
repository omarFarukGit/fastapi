from pymongo import MongoClient


client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")

db = client["your_db"]
collection = db["users"]  # ✅ Remains open for FastAPI routes to use