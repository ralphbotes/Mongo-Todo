from pymongo import MongoClient
import datetime

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

# Set todo in dictionary form
todo1 = {
    "name": "Ralph", "text": "My first todo!", "status": "open",
    "tags": ["python", "coding"], "date": datetime.datetime.utcnow()
}

# Set where new todo needs to go, its future location
todos = db.todos

# Insert one to location
result = todos.insert_one(todo1)

# Set multiples
todo2 = [{"name": "Karen", "text": "My second todo!", "status": "open",
    "tags": ["python", "coding"], "date": datetime.datetime.utcnow()},
    {"name": "Rene", "text": "My third todo!", "status": "open",
    "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}]

# Insert many to location
result = todos.insert_many(todo2)