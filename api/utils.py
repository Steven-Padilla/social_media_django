from pymongo.mongo_client import MongoClient
import urllib
import environ
env = environ.Env()
environ.Env.read_env()




uri = "mongodb+srv://steven:" + urllib.parse.quote('$CU4pM3@*KegnNB') + "@socialmedia.u9azysb.mongodb.net/?retryWrites=true&w=majority&appName=" + env('MONGO_APP')

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)