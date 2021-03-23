
from flask import  Flask,jsonify,request
from flask_cors import CORS
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

conn = sqlite3.connect('test.db')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/api/v1/DummyApi/", methods=['GET'])
def DummyApi():
    list = [{'Name': 'Badruzzaman'}, {'Name': 'Rahim'}]
    return jsonify(list),200

@app.route("/api/v1/Register/", methods=['POST'])
def Registration():
    FIRSTNAME = request.json('FIRSTNAME')
    LASTNAME = request.json('LASTNAME')
    EMAIL = request.json('EMAIL')
    PHONE = request.json('PHONE')
    firstName = request.json('firstName')
    conn.execute("INSERT INTO Users (ID,FIRSTNAME,LASTNAME,EMAIL,PHONE) \
          VALUES (1, 'BADRU', 'ZAMAN', 'badru.cse@gmail.com', '+8801719730475')");
    conn.commit()
    return jsonify(list),200

if __name__ == "__main__":
    app.run()