from flask import Flask, Response, jsonify, render_template
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import json


app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'
# Use flask_pymongo to set up mongo connection
# Local MongoDB connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/dogs"

# Web Hosted MongoDB
app.config["MONGO_URI"] = "mongodb+srv://admin:N!ck40o0@sampleapicluster.xkn27.mongodb.net/dogs?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/', methods=["GET", "POST"])
def root():
    # return render_template('index.html')
    return app.send_static_file("index.html")


@app.route("/loadDB/", methods=["GET"])
def index():
    dogcollection = mongo.db.alldogs 
    dogcollection.drop()
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    responseJson = response.json()
    dogcollection.insert_one(responseJson)


@app.route("/allbreeds/", methods=['GET', 'POST'])
@cross_origin()
def allbreeds():
    dogdb = mongo.db.alldogs
    alldogs = dogdb.find({})
    dogsjson = json.loads(json_util.dumps(alldogs))
    return jsonify(dogsjson)

if __name__ == "__main__":
    app.run()
