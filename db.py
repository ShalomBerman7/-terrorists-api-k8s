from pymongo import MongoClient


def insert_mongodb(data):
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    try:

        db = client.get_database("MONGO_INITDB_DATABASE")
        collection = db.get_collection("threat_db")

        result = collection.insert_many(data['top'])
        print(len(result.inserted_ids))

        client.close()

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
