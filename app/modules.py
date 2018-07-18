from app import mongo
import pymongo
from flask import render_template, flash, redirect


class item():
    def save_item(self, itemname, ava, kind, haben):
        newThing = {
            "_id": itemname,
            "art": ava,
            "kind" : kind,
            "haveit": haben
        }
        try:
            result = mongo.db.items.insert_one(newThing)
            print(result)
        except pymongo.errors.DuplicateKeyError:
            flash('Item gibt es schon!')
    def read_items(self):
        #TODO lesen einbauen ( in arbeit)
        dinge = mongo.db.items.find()
        return dinge
    def filter(self, was):
        dinge = mongo.db.items.find(was)
        return dinge