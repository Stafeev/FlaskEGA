__author__ = 'artemstafeev'
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict
from flask import Flask,request,render_template
import jinja2
import os
import json

JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)
db = SqliteExtDatabase('users_database.db')
app = Flask(__name__,static_folder="templates/static",
            template_folder="templates")
template = JINJA_ENVIRONMENT.get_template('templates/index.html')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()
    phoneNumber = CharField()

# main endpoint
@app.route('/', methods=['GET'])
def mainHandler():
    return render_template('index.html')
# Show all names endpoint
@app.route('/users', methods=['GET'])
def showUsers():
    # if 'name' parameter is presented then we query by name
    # otherwise we return all records
    if (request.form.get('name')):
        name = request.form.get('name')
        user = User.get(User.username == name)
        return json.dumps(model_to_dict(user))
    else:
        users = []
        for user in User.select():
            users.append(model_to_dict(user))
        return json.dumps(users)
# Create user endpoint
@app.route('/create', methods=['PUT'])
def createUser():
    # if 'name' parameter is presented then we query by name
    # otherwise we return all records
    if (request.form.get('name') and request.form.get('phone')):
        user = User.create(username=request.form.get('name'), phoneNumber=request.form.get('phone'))
        return json.dumps(model_to_dict(user))
    else:
        return 'Please supply phone and name parameters'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
