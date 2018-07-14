from app import mongo
import pymongo
from flask import render_template, flash, redirect


class item():
    def save_item(self, itemname, ava, kind, haben):
        print(itemname, ava, haben)
        newThing = {
            "_id": itemname,
            "class": ava,
            "kind" : kind,
            "haveit": haben
        }
        try:
            result = mongo.db.items.insert_one(newThing)
        except pymongo.errors.DuplicateKeyError:
            flash('Item gibt es schon!')
