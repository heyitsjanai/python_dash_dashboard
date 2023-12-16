from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-coded to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        
        #
        # Connection Variables
        # USER = 'aacuser'  --user needs to input these values themselves
        # PASS = 'passWord' --USER & PASS must match these values to authenticate
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30803
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]
        print("Connected to Austin Animal Center Database")  # validates connection

    # Method to CREATE a data object in the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("Animal added successfully")  # validates data has been added
        else:
            raise Exception("Nothing to save because data parameter is empty")

    # Method that READS a data entry from database
    def read(self, query):
        if query is not None:
            results = self.database.animals.find(query)
        else:
            results = self.database.animals.find()
        data = [result for result in results]
        return data

    # Method that finds the query object and UPDATES it using update data
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            self.database.animals.update_many(query, {"$set": update_data})
            print("Animal information updated successfully")
        else:
            raise Exception("Nothing to update because query or update_data parameters are empty")

    # Method that DELETES a data object
    def delete(self, query):
        if query is not None:
            self.database.animals.delete_many(query)
            print("Animal deleted successfully")
        else:
            raise Exception("Nothing to delete, because query parameter is empty")