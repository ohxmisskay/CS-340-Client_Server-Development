#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 04:41:13 2023

@author: winniekwong_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #USER = 'aacuser'
        #PASS = '5H1RO2018'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32077
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        #Returns True if a succesful instead, else False
        try:
            if data is not None:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            else:
                raise Exception("Nothing to save, because data parameter is empty")
        except:
            return False
            
# Create method to implement the R in CRUD.
    def read(self, searchData):
        #Returns results in a list if command is successful
        if searchData:
            data = self.database.animals.find(searchData, {"_id": 0})
        else:
            data = self.database.animals.find({}, {"_id": 0})
            return False
        return data

# Create method to implement the U in CRUD.  
    def update(self, searchData, updateData):
        try:
            if searchData is not None:
                result_update = self.database.animals.update_many(searchData, {"$set": updateData })
                print (result_update.modified_count, "request complete.")
                
            else:
                raise Exception("Nothing to update, because data parameter is empty")
        except:
            return False

# Create method to implement the D in CRUD. (removing a section)  
    def delete(self, searchData, deleteData):
        try:
            if searchData is not None:
                result_remove = self.database.animals.update_many(searchData, {"$unset": deleteData })
                print (result_remove.modified_count, "request complete.")
            else: 
                raise Exception("Nothing to delete, because data parameter is empty")
                
        except: 
            return False
            
        