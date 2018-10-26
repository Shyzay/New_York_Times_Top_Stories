import pymongo
from datetime import datetime



myclient = pymongo.MongoClient("mongodb://localhost:27017/")


class DataBase(object):
    ''' A Class That Stores all the database'''

    def __init__(self):
        #intialise the object and set properties
        self.database_name = myclient["nytimestopstories"]
        self.database_collection = self.database_name["articles"]
        self.data_value={}
        #Properties that help in actual storing it to mongo
        self.data_storage=None


    def insert_data(self,ny_list,time):
         '''Function to insert database'''

        #check if data already exist in the database
        #then just update

         if(self.database_collection.count()>=1):
              #gets rid of all datas first

               self.data_storage=self.database_collection.delete_many({})
               #insert the data
               self.data_value['articles']=ny_list
               self.data_value['time']=time
               self.data_storage=self.database_collection.insert_one(self.data_value)

               pass
        #else insert the data
         else:
             self.data_value['articles']=ny_list
             self.data_value['time']=time


             self.data_storage=self.database_collection.insert_one(self.data_value)




    #retrieve data

    def retrive_data(self):
        ''' function to return the article details'''

        ny_datas =list(self.database_collection.find())
        return ny_datas


  #function to fetch out time and return a boolean value
    def is_greater_than_cach_time(self,new_time):
        '''method that return a boolean value determining if the time is less or greater than 5min'''
        ny_data=self.retrive_data()
        #get the old time the data was inserted
        old_time=ny_data[0]['time']

        time_delta = new_time - old_time
        #convert it to min
        time_checker= int((time_delta.days + time_delta.seconds)/60)
        #check if it is greater than 5 min or not
        if(time_checker<5):
            return True
        else:
            return False



