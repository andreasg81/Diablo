import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Diablorocks'
    MONGO_URI = "mongodb://slave:s1emens@10.0.0.147:27017/Controll?authSource=Controll"
    AVATARS = [
        ('Barbar', 'Barbar'),
        ('Dämonenjäger', 'Dämonenjäger'),
        ('Hexendoktor', 'Hexendoktor'),
        ('Kreuzritter', 'Kreuzritter'),
        ('Mönch', 'Mönch'),
        ('Totenbeschörer','Totenbeschörer'),
        ('Zauberer', 'Zauberer')
    ]
    ITEM_KIND = [
        ('Gewand', 'Gewand'),
        ('Schmuck', 'Schmuck'),
        ('Waffe', 'Waffe')
    ]