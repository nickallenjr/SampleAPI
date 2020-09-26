from flask import Flask, render_template, redirect, url_for, Response, jsonify
from bson import json_util
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import json


app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/dogs"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#This is not recommended in production
#What would happen is every time you visit the root route it would load the DB again with all the data
#
@app.route("/", methods=["GET"])
def index():
    dogcollection = mongo.db.alldogs 
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    # print(response.json())
    responseJson = response.json()
    dogcollection.insert(responseJson)
    # return render_template("index.html", mars=mars)


@app.route("/allbreeds/", methods=['GET'])
@cross_origin()
def allbreeds():
    dogdb = mongo.db.alldogs
    # mars_data = scrape_mars.scrape_all()
    # mars.update({}, mars_data, upsert=True)
    alldogs = dogdb.find({})
    dogsjson = json.loads(json_util.dumps(alldogs))
    return jsonify(dogsjson)

if __name__ == "__main__":
    app.run()
