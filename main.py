


from flask import  Flask,jsonify,request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)


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


#https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
@app.route("/Register", methods=['POST'])
def Register():

    try:
         conn = sqlite3.connect('test.db')
         cursor = conn.cursor()
         request_data = request.get_json()
         FIRSTNAME = request_data['FirstName']
         LASTNAME = request_data['LastName']
         EMAIL = request_data['Email']
         PHONE = request_data['Phone']
         #cursor.execute("create table people (name_last, age)")
         who = "Yeltsin"
         age = 72
         conn.execute("insert into people values (?, ?)", (who, age))
         conn.execute("INSERT INTO Users VALUES (?, ? , ?, ?, ?)", (3, FIRSTNAME,LASTNAME,EMAIL,PHONE))
         conn.commit()
         #cursor.execute("INSERT INTO Users (ID,FIRSTNAME,LASTNAME,EMAIL,PHONE) \
                   #VALUES (FIRSTNAME, LASTNAME, EMAIL, PHONE)");
         #conn.commit()
    except ValueError:
        print(ValueError)

    return jsonify(request_data),200

if __name__ == "__main__":
    app.run()