from peewee import *
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('entries', user='postgres')

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

    DATABASE.create_tables( [Users, Entries], safe=True)
    print("Connected to the DB and created tables")

    DATABASE.close()