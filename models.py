from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

DATABASE = connect(os.environ.get('DATABASE_URL') or PostgresqlDatabase('entries', user='postgres'))
# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.

class Users(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE



class Entries(Model):
    title = CharField()
    date = DateField()
    description = CharField()
    decision = CharField()
    keywords = CharField()
    foreign_key = ForeignKeyField(Users, backref='my_entries', null=True)

    class Meta:
        database = DATABASE



def initialize():
    DATABASE.connect()

    DATABASE.create_tables([Users, Entries], safe=True)
    print("Connected to the DB and created tables")

    DATABASE.close()