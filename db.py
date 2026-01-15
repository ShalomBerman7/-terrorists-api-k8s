from pymongo import MongoClient

try:
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)

    client.admin.command("ping")
    print("Connected successfully")

    # other application code

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
