import pymongo
import pandas
from bson.son import SON


URI = 'mongodb+srv://benoitfavrie:benito@cluster0.swglflt.mongodb.net/' # Change ça avant de faire le TP 
client = pymongo.MongoClient(URI) 
db = client.sample_restaurants
restaurants = db.restaurants