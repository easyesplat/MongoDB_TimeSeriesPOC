from pymongo import MongoClient
from config import CONNECTION_STRING

def get_database():
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   # IMPORTANT: Utilized own personal MongoDB Atlas connection string; Didn't push it to Github due to privacy.
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['sensor_data']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()