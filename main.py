
from flask import  Flask,jsonify,request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('test.db')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/api/v1/DummyApi/", methods=['GET'])
def DummyApi():
    list = [{'Name': 'Badruzzaman'}, {'Name': 'Rahim'}]
    return jsonify(list),200

@app.route("/api/v1/Create/<string:firstname>", methods=['POST'])
def Create(firstname):
    #firstName = request['firstname']
   #conn.execute("INSERT INTO Users (ID,FIRSTNAME,LASTNAME,EMAIL,PHONE) \
          #VALUES (1, 'BADRU', 'ZAMAN', 'badru.cse@gmail.com', '+8801719730475')");
    #conn.commit()
    return jsonify(name = firstname),200

if __name__ == "__main__":
    app.run()