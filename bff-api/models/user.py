from mongoengine import *

class User(Document):
    username = StringField(required=True)
    income = ListField()
    vale = ListField()
