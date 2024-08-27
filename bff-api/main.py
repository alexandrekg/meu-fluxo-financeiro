from fastapi import FastAPI
from settings import DATABASE_NAME

import mongoengine as mongo
from models.user import User

app = FastAPI()

@app.get('/')
def _main():
    mongo.connect(DATABASE_NAME, host='127.0.0.1', port=27017)

    cursor = User.objects()
    return [c for c in cursor]


@app.post('/create_user')
def _main():
    mongo.connect(DATABASE_NAME, host='127.0.0.1', port=27017)

    user = User(username='user')
    user.save()
