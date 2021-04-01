
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
#https://docs.python.org/3/library/sqlite3.html
@app.route("/api/v1/Register/", methods=['POST'])
def Register():

    try:
         conn = sqlite3.connect('BGIT.db')
         request_data = request.get_json()

         FullName = request_data['FullName']
         Email = request_data['Email']
         Mobile = request_data['Mobile']

         #conn.execute('''CREATE TABLE Users( Id INTEGER PRIMARY KEY AUTOINCREMENT,FULLNAME TEXT NOT NULL,EMAIL TEXT NOT NULL,MOBILE TEXT)''')

         conn.execute("INSERT INTO Users (FULLNAME, EMAIL,MOBILE) VALUES (?, ?, ?)", (FullName, Email, Mobile))
         conn.commit()
         conn.close()
         
         #cursor.execute("INSERT INTO Users (ID,FIRSTNAME,LASTNAME,EMAIL,PHONE) \
                   #VALUES (FIRSTNAME, LASTNAME, EMAIL, PHONE)");
         #conn.commit()
    except ValueError:
        print(ValueError)
    return jsonify(request_data),200


@app.route("/api/v1/AboutPost/", methods=['POST'])
def AboutPost():
    try:
        conn = sqlite3.connect('BGIT.db')
        request_data = request.get_json()
        Description = request_data['Description']
        conn.execute("UPDATE About SET ISACTIVE = 0 WHERE ISACTIVE = 1")
        conn.commit()
        conn.execute("INSERT INTO About (DESCRIPTION, ISACTIVE) VALUES (?, ?)", (Description, 1))
        conn.commit()
        conn.close()
    except ValueError:
        print(ValueError)
    return jsonify(request_data), 200

@app.route("/api/v1/About/", methods=['GET'])
def About():
    try:
        conn = sqlite3.connect('BGIT.db')
        cursor = conn.execute("SELECT Id, DESCRIPTION, ISACTIVE FROM About WHERE ISACTIVE = 1")
        for row in cursor:
            response_data = [{'Id':  int(row[0]), "Description": row[1],"IsActive" : row[2]}]
    except ValueError:
        print(ValueError)
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run()