from peewee import *
from flask_login import UserMixin



class Users(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db



class Entries(Model):
    title = CharField()
    date = DateField()
    description = CharField()
    decision = CharField()
    keywords = CharField()
    foreign_key = ForeignKeyField()

    class Meta:
        database = db



def initialize():
    db.connect()

    db.create_tables( [Users, Entries], safe=True)
    print("Connected to the DB and created tables")

    db.close()